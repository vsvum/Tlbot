import telebot
import webbrowser

bot = telebot.TeleBot("8247222389:AAGnNEyuC0ob1KqZ7Xh0Hm5zMgTjEuTkCLU")

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open("https://ru.pinterest.com/ideas/красивые-котики/926883209594/")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Хорошо дела")




bot.polling(none_stop=True)