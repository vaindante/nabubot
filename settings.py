import logging
import os
import sys

import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
log = telebot.logger

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(os.getenv('LOGGING_LEVEL_TO_CONSOLE', 'WARN'))
# Устанавливаем формат сообщений
console_handler.setFormatter(
    '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"')

log.addHandler(console_handler)

log.setLevel(20)
