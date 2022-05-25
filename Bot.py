import telebot
from BotToken import token
from workWithDB import Sqlighter
from telebot import types


def reply_check(message):
    if message.text == "Написать отзыв ✍️":
        return True
    elif message.text == "Список услуг 📃":
        return True
    elif message.text == "Поддержка ⚙️":
        return True
    else:
        return False


def review(message):
    Sqlighter.save_review(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Спасибо! отзывы помогут нам развиваться! 😁")


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"], chat_types=["private"])
def sendler(message):
    if Sqlighter.get_info_workers(message.from_user.id) is None:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        get_list = types.KeyboardButton("Список услуг 📃")
        write_review = types.KeyboardButton("Написать отзыв ✍️")
        support = types.KeyboardButton("Поддержка ⚙️")
        kb.add(get_list, write_review, support)
        bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}, "
                                          f"я бот компании *Электротехник*"
                         , parse_mode="markdown", reply_markup=kb)


@bot.message_handler(func=reply_check)
def send_reply(message):
    if message.text == "Написать отзыв ✍️":
        sent = bot.send_message(message.chat.id, "Напишите отзыв ✍️")
        bot.register_next_step_handler(sent, review)
    elif message.text == "Список услуг 📃":
        pass
    elif message.text == "Поддержка ⚙️":
        pass


@bot.message_handler(content_types=["text"], chat_types=["group"])
def text_checkker(message):
    text = message.text
    if "мат" in text.lower():
        bot.send_message(message.chat.id, "не материтесь")


bot.infinity_polling()
