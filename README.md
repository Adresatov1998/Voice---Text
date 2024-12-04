# Voice -> Text
**Description**
<br>
This project is a Telegram bot that recognizes voice messages and converts them into text. The bot uses the speech_recognition library for audio processing and pydub for audio file conversion. It also utilizes the telebot library to interact with the Telegram API.

**Installation**
1. Ensure you have Python 3.6 or higher installed.

2. Install the required libraries by running the following command:
```pip install pyTelegramBotAPI pydub SpeechRecognition```
3. Install FFmpeg, which is necessary for working with audio files. Installation instructions can be found on the <a src="https://ffmpeg.org/download.html">official FFmpeg website</a>

**Configuration**
1. Obtain a token for your bot by creating it through BotFather on Telegram.
2. Replace the line bot = telebot.TeleBot('Your Bot Token') with your token.

**Usage**
1. Run the script: ```python Voice - Text.py```
2. Open Telegram and find your bot.
3. Send a voice message to the bot, and it will respond with the transcribed text.

**Functionality**
1. The bot processes voice messages and converts them into text.
2. The recognized text is automatically punctuated.
3. In case of an error, the bot notifies the user about the issue.

**Commands**
 - /start - A welcome message and instructions on how to use the bot.

**Notes**
 - The bot runs in an infinite loop and processes voice messages in a separate thread.
 - Please ensure a stable internet connection for proper operation.

<div align="center"><h1>© LLC "Server.System company", 2023-2024</h1></div>
