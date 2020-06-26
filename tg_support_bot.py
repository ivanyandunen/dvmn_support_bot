from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from dotenv import load_dotenv
import os
from dialogflow import detect_intent_texts


load_dotenv()


def start(bot, update):
    update.message.reply_text('Здравствуйте')


def help(bot, update):
    update.message.reply_text('Help!')


def echo(bot, update):
    text = detect_intent_texts(
        os.getenv("PROJECT_ID"),
        update.message.from_user['id'],
        update.message.text
    )
    update.message.reply_text(text.query_result.fulfillment_text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(os.getenv('TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    main()
