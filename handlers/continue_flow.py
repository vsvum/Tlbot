from bot import bot
from keyboards.inline import get_continue_keyboard

# Данные для второго шага
SECOND_PHOTO = "photos/step2_image.jpg"
SECOND_TEXT = """
🎯 <b>Отлично, ты перешёл ко второму шагу!</b>

Здесь — следующая порция контента.
Можно добавлять сколько угодно шагов по аналогии.
"""

@bot.callback_query_handler(func=lambda call: call.data == "step_2")
def handle_step_2(call):
    # Удаляем кнопку "Продолжить" у предыдущего сообщения (опционально)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    
    # Отправляем второй шаг
    with open(SECOND_PHOTO, "rb") as photo:
        bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=SECOND_TEXT,
            reply_markup=get_continue_keyboard("step_3")  # Для следующего шага
        )