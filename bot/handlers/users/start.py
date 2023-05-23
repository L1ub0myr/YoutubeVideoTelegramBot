from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_name = message.from_user.first_name if message.from_user.first_name != '' else 'Сонечко'
    await message.delete()
    await message.answer_sticker('CAACAgIAAxkBAAEI7fBkWzULZKeK31wJo8YYIcXa7b4tpgACAQEAAladvQoivp8OuMLmNC8E')
    await message.answer(f"Привіт {user_name}, як справи?")
