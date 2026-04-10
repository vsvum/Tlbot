from bot import bot
from keyboards.inline import get_continue_keyboard

# Путь к фото (локальный или URL)
FIRST_PHOTO = "photos/photo.jpg"  # или https://...
FIRST_TEXT = """
👋 <b>Доброе утро моя дорогая!</b>

Я знаю что вам очень сильно понравились цветочки, но как вы поняли это не все. 
Нажмите пожалуйста кнопочку продолжить.
И я очень сильно вас прошу сделать все что там будет сказано. 
Ведь я очень сильно сторался сделать этот день чуть чуть особенным.

"""

@bot.message_handler(commands=["start"])
def send_first_step(message):
    # Отправляем фото + текст + кнопку
    with open(FIRST_PHOTO, "rb") as photo:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=FIRST_TEXT,
            reply_markup=get_continue_keyboard("step_2")
        )   