from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from dotenv import load_dotenv
import os
from dialogflow import detect_intent_texts
from tg_logger import TgHandler


logger = logging.getLogger('Logger')

def start(bot, update):
    update.message.reply_text('Здравствуйте')


def reply_to_message(bot, update):
    text = detect_intent_texts(
        os.getenv("DIALOGFLOW_PROJECT_ID"),
        f'tg-{update.message.from_user['id']}',
        update.message.text
    )
    update.message.reply_text(text.query_result.fulfillment_text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(os.getenv('TG_TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, reply_to_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':

    load_dotenv()
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger.addHandler(TgHandler())
    main()
