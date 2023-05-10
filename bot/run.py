from aiogram import types, Dispatcher, executor

import handlers
from loader import dp, bot
from config import ADMIN


async def on_startup(dispatcher: Dispatcher):
    await bot.send_message(ADMIN, 'Bot started')


async def on_shutdown(dispatcher: Dispatcher):
    await bot.send_message(ADMIN, 'Bot stopped')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
