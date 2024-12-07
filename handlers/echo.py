# echo.py
from aiogram import types, Dispatcher

async def echo_handler(message: types.Message):
    text = message.text
    if text.isdigit():
        n = int(text)
        result = n ** 2
        await message.answer(result)
    else:
        await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)