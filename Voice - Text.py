import os
import time
import telebot
from pydub import AudioSegment
import speech_recognition as sr
from queue import Queue
from threading import Thread
import re
import datetime
now = datetime.datetime.now()
current_year = now.year
bot = telebot.TeleBot('Токен бота')
voice_queue = Queue()
while True:
    try:
        def process_voice_messages():
            while True:
                message = voice_queue.get()
                if message is None:
                    break
                handle_voice(message)
                voice_queue.task_done()
        def punctuate_text(text):
            text = re.sub(r'([.!?])', r'\1 ', text)
            text = re.sub(r'(\w+)(\s+)(и|или|но)(\s+)', r'\1, \3 ', text)
            if text and text[-1] not in '.!?':
                text += '.'
            return text
        def handle_voice(message):
            try:
                file_info = bot.get_file(message.voice.file_id)
                file = bot.download_file(file_info.file_path)
                with open('temp.ogg', 'wb') as f:
                    f.write(file)
                AudioSegment.from_file('temp.ogg').export('temp.wav', format='wav')
                os.remove('temp.ogg')
                r = sr.Recognizer()
                with sr.AudioFile('temp.wav') as source:
                    audio = r.record(source)
                    try:
                        text = r.recognize_google(audio, language='ru-RU')
                    except sr.UnknownValueError:
                        text = None
                    except sr.RequestError as e:
                        print(f"Ошибка API: {e}")
                        text = None
                os.remove('temp.wav')
                if text:
                    punctuated_text = punctuate_text(text)
                    bot.send_message(message.chat.id, f'<b>Расшифрованное сообщение:</b>\n<blockquote><i>{punctuated_text}</i></blockquote>', reply_to_message_id=message.message_id, parse_mode='HTML')
                else:
                    bot.send_message(message.chat.id, '*Невнятный шум.*', reply_to_message_id=message.message_id)
            except Exception as e:
                print(f"Ошибка при обработке сообщения: {e}")
                bot.send_message(message.chat.id, '*Произошла ошибка при обработке вашего сообщения.*', reply_to_message_id=message.message_id)
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            welcome_text = (
                "Приветик! Я бот для распознавания голосовых сообщений.\n"
                "Отправьте мне голосовое сообщение, и я расшифрую его в текст.\n-----\n"
                f"© ООО «<a href='https://www.serversys.ru'>Server.System company</a>», 2023-{current_year}"
            )
            bot.send_message(message.chat.id, welcome_text, parse_mode='HTML')
        @bot.message_handler(content_types=['voice'])
        def enqueue_voice(message):
            voice_queue.put(message)
        thread = Thread(target=process_voice_messages)
        thread.start()
        bot.polling(none_stop=True)
        thread.join()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)