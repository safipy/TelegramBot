from aiogram import types

async def is_admin(message: types.Message):
    """
    бработчик для определения админа в чате.
    """
    print(message.from_user)
    author = message.from_user.id
    admins = await message.chat.get_administrators()
    not_admin = False
    for admin in admins:
        if admin["user"]["id"] == author:
            not_admin = True
            break
    return not_admin


async def bad_words(message: types.Message):
    """
    Обработчик для проверки запрещенных слов!
    """
    b_words = ("тупой", "дурак", "идиот", "мерзавец")
    if message.chat.type != 'private':
        for word in b_words:
            if word in message.text.lower().replace(' ', '').count(word):
                await message.answer(f"{message.from_user.first_name},"
                                    f" не используй запрещенную лексику!")
                break


async def ban_user(message: types.Message):
    """
    Обработчик, чтоб банить пользователя в чате
    через команду
    """
    if message.chat.type != 'private':
        admin_author = await is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )