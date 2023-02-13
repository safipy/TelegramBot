from aiogram import types
from config import bot

kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("iphone")
)
in_kb = types.InlineKeyboardMarkup()
in_kb.add(types.InlineKeyboardButton(
    text="14 Pro Max",
    callback_data="smartphone"
))
in_kb.add(types.InlineKeyboardButton(
    text="13 Pro Max",
    callback_data="smartphone"
))
kb.add(
    types.KeyboardButton("samsung")
)
in_kb_s = types.InlineKeyboardMarkup()
in_kb_s.add(types.InlineKeyboardButton(
    text="Samsung GALAXY S23",
    callback_data="smartphone"
))
in_kb_s.add(types.InlineKeyboardButton(
    text="Samsung GALAXY S22",
    callback_data="smartphone"
))


async def show(call: types.CallbackQuery):
    await call.message.answer(
        text="Выберите товар:",
        reply_markup=kb
    )


async def show_iphone(message: types.Message):
    await message.reply(
      text="Какая модель iphona вам нужна?",
      reply_markup=in_kb
    )

async def show_samsung(message: types.Message):
    await message.reply(
      text="Какая модель Samsung вам нужна?",
      reply_markup=in_kb_s
    )

