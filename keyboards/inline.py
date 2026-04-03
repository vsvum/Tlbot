from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_continue_keyboard(callback_data: str = "next_step"):
    """Создаёт inline-клавиатуру с кнопкой 'Продолжить'"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("▶️ Продолжить", callback_data=callback_data))
    return markup