from bot import bot
from keyboards.inline import get_continue_keyboard

# Путь к фото (локальный или URL)
FIRST_PHOTO = "photos/qr.jpg"  # или https://...
FIRST_TEXT = """
👋 <b>Привет!</b>

Это первый шаг твоего путешествия.

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