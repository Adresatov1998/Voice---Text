# Voice---Text
**Description**
This project is a Telegram bot that recognizes voice messages and converts them into text. The bot uses the speech_recognition library for audio processing and pydub for audio file conversion. It also utilizes the telebot library to interact with the Telegram API.

**Installation**
1. Ensure you have Python 3.6 or higher installed.

2. Install the required libraries by running the following command:
```pip install pyTelegramBotAPI pydub SpeechRecognition```
3. Install FFmpeg, which is necessary for working with audio files. Installation instructions can be found on the official FFmpeg website.

**Configuration**
Obtain a token for your bot by creating it through BotFather on Telegram.
Replace the line bot = telebot.TeleBot('Your Bot Token') with your token.
