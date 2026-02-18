import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from groq import GROQ

token = os.environ['TOKEN']
api_key = os.environ['GROQ_API_KEY']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='مرحباً! أنا بوت تلجرام ذكي')

def main():
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()