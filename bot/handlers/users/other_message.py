from aiogram import types

from loader import dp


@dp.message_handler()
async def other_message(message: types.Message):
    await message.delete()
    await message.answer("Я вас не зрозумів 😥. Перевірте чи ви все правильно написали")
