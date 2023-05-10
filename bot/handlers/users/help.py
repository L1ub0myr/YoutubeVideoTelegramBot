from aiogram import types

from loader import dp


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.delete()
    await message.answer(f"Я вмію завантажувати аудіо та відео з YouTube. 💾\n"
                         f"Просто киньте мені посилання на YouTube відео, "
                         f"яке потрібно завантажити")
