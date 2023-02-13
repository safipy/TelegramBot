from aiogram import types
import random




#@dp.message_handler(commands=["picture"])
async def image(message: types.Message):
    image = ["photo/jerry.jpg", "photo/jer.jpeg"]
    photo = open(random.choice(image), 'rb')
    await message.answer_photo(
        photo
    )

#@dp.message_handler()
async def echo(message: types.Message):
    c = len(message.text)
    if c >= 3:
        await message.answer(
           message.text.upper()
        )
    else:
        await message.answer(
            message.text
        )