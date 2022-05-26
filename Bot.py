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


def service_checker(message):
    if message.text == "1":
        reg = bot.send_message(message.chat.id,
                                    "Вы заказали услугу 'Провести электричество в дом' \nВ следующем сообщении отравьте через пробел ваш номер телефона, адрес и дату\n"
                                    "Пример:\n"
                                    "89992576336, Улица Пушкина дом 4 квартира 25, 01.06.2022")
        bot.register_next_step_handler(reg, reg_serv)
    elif message.text == "2":
        reg = bot.send_message(message.chat.id,
                              "Вы заказали услугу 'Дизайнерские лампы для вашего дома' \nВ следующем сообщении отравьте через пробел ваш номер телефона, адрес и дату\n"
                              "Пример:\n"
                              "89992576336, Улица Пушкина дом 4 квартира 25, 01.06.2022")
        bot.register_next_step_handler(reg, reg_serv)
    elif message.text == "3":
        reg = bot.send_message(message.chat.id,
                               "Вы заказали услугу 'Установка кондиционеров' \nВ следующем сообщении отравьте через пробел ваш номер телефона, адрес и дату\n"
                               "Пример:\n"
                               "89992576336, Улица Пушкина дом 4 квартира 25, 01.06.2022")
        bot.register_next_step_handler(reg, reg_serv)
    elif message.text == "4":
        reg = bot.send_message(message.chat.id,
                               "Вы заказали услугу 'Подключение умного дома' \nВ следующем сообщении отравьте через пробел ваш номер телефона, адрес и дату\n"
                               "Пример:\n"
                               "89992576336, Улица Пушкина дом 4 квартира 25, 01.06.2022")
        bot.register_next_step_handler(reg, reg_serv)


def reg_serv(message):
    text = message.text
    text = text.split(", ")
    if len(text)==3:
        Sqlighter.save_order("Провести электричество в дом", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)
    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv)


def reg_serv2(message):
    text = message.text
    text = text.split(", ")
    if len(text)==3:
        Sqlighter.save_order("Дизайнерские лампы для вашего дома", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)
    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv2)



def reg_serv3(message):
    text = message.text
    text = text.split(", ")
    if len(text)==3:
        Sqlighter.save_order("Установка кондиционеров", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)
    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv3)


def reg_serv4(message):
    text = message.text
    text = text.split(", ")
    if len(text)==3:
        Sqlighter.save_order("Подключение умного дома", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)
    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv4)


def review(message):
    Sqlighter.save_review(message.text)
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
        photo = open("services.png", "rb")
        first = bot.send_photo(message.chat.id, photo, "Наши услуги")
        bot.register_next_step_handler(first, service_checker)
    elif message.text == "Поддержка ⚙️":
        bot.send_message(message.chat.id, "Пишите на телеграмм @GGAMID")


@bot.message_handler(commands=["start"], chat_types=["group"])
def sendler(message):

    bot.send_message(message.chat.id, f"Здравствуйте,"f"я бот компании *Электротехник*"
                                      f" и я буду следить за порядком в чате!", parse_mode="markdown", reply_markup=None)


@bot.message_handler(content_types=["text"], chat_types=["group"])
def text_checkker(message):
    text = message.text
    if "мат" in text.lower():
        bot.send_message(message.chat.id, "не материтесь!")





bot.infinity_polling()
