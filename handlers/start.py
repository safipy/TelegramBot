from aiogram import types

in_kb = types.InlineKeyboardMarkup()
in_kb.add(types.InlineKeyboardButton(
    text="Наши товары:",
    callback_data="smartphone"
))

# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(
        f"Привет, {user} ",
        reply_markup=in_kb
    )


# @dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        """
/start - Приветствие
/help - Функции Бота
/myinfo - Ваши личные данные
/picture - Картинка для хорошего настроения
      """
    )


# @dp.message_handler(commands=["myinfo"])
async def info(message: types.Message):
    user_firstname = message.from_user.first_name
    user_name = message.from_user.username
    user_id = message.from_user.id
    await message.answer(
        f"Ваше имя - {user_firstname} "
        f"\nВаше имя пользователя - {user_name} "
        f"\nВаш id - {user_id} "
    )
