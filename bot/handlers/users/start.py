from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.delete()
    await message.answer_sticker('CAACAgIAAxkBAAEI7fBkWzULZKeK31wJo8YYIcXa7b4tpgACAQEAAladvQoivp8OuMLmNC8E')
    await message.answer(f"Привіт {message.from_user.first_name}")
