import logging
import os
from telegram import Bot

class TgHandler(logging.Handler):


    def __init__(self):
        super().__init__()
        self.bot = os.getenv('TG_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(self.chat_id, text=log_entry)
