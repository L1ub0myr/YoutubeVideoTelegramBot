from pytube import exceptions, YouTube
from aiogram import types

from loader import dp
from misc.download_files import Video


def check_user_link(link: str):
    try:
        YouTube(link)
        return True
    except exceptions.RegexMatchError:
        return False


@dp.message_handler(lambda message: check_user_link(message.text))
async def download_files(message: types.Message):
    await message.delete()
    video = Video(message.text)
    await message.answer(f'Інформація про відео:\nНазва: <b>{video.name}</b>\nАвтор: <b>{video.autor}</b>')
    await download_audio(message, video)


async def download_audio(message: types.Message, video: Video):
    try:
        await message.answer("<b>ЗАВАНТАЖЕННЯ РОЗПОЧАЛОСЬ</b> ▶️\nБудь ласка, трішки зачекайте 😘")
        video.download_audio()
        await message.answer('<b>ГОТОВО</b> ✅')
        await message.answer('<b>НАДСИЛАЮ</b> ✉️')
        await message.answer_audio(open(f'{video.name}.mp3', 'rb'), performer=video.autor,
                                   duration=video.length, title=video.name)
    except Exception as ex:
        print(ex)
        await message.answer("Вибачте, виникла похибка у роботі програми.\nСпробуйте ще раз")
    finally:
        video.delete_audio()
