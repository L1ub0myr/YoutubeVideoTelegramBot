from aiogram import types, Dispatcher, Bot

from config import TOKEN


bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
