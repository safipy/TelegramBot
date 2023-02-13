from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.start import(
    start,
    help,
    info
)
from handlers.echo import(
    echo,
    image
)
from handlers.smartphone import (
    show,
    show_iphone,
    show_samsung
)

if __name__ == "__main__":
    print(__name__)

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(info, commands=["myinfo"])
    dp.register_message_handler(image, commands=["picture"])
    dp.register_callback_query_handler(show, Text(startswith="smartphone"))
    dp.register_message_handler(show, commands=["smartphone"])
    dp.register_message_handler(show_iphone, Text(startswith="iphone"))
    dp.register_message_handler(show_samsung, Text(startswith="samsung"))
    dp.register_message_handler(echo)


    executor.start_polling(dp)
