import time
import telebot
from BotToken import token
from workWithDB import Sqlighter
from telebot import types
from threading import Thread
from experiments import sendler_notification_holiday, sendler_notification_peregovorka, sendler_notification_salary
from workWithDB import get_data




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

    if len(text) == 3:
        Sqlighter.save_order("Провести электричество в дом", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)

    elif message.text == "Поддержка ⚙️" or message.text == "Список услуг 📃" or message.text == "Напишите отзыв ✍️":
        bot.send_message(message.chat.id, "Отправьте сообщение еще раз")

    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv)


def reg_serv2(message):
    text = message.text
    text = text.split(", ")
    if len(text) == 3:
        Sqlighter.save_order("Дизайнерские лампы для вашего дома", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)

    elif message.text == "Поддержка ⚙️" or message.text == "Список услуг 📃" or message.text == "Напишите отзыв ✍️":
        bot.send_message(message.chat.id, "Отправьте сообщение еще раз")

    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv2)


def reg_serv3(message):
    text = message.text
    text = text.split(", ")
    if len(text) == 3:
        Sqlighter.save_order("Установка кондиционеров", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)

    elif message.text == "Поддержка ⚙️" or message.text == "Список услуг 📃" or message.text == "Напишите отзыв ✍️":
        bot.send_message(message.chat.id, "Отправьте сообщение еще раз")

    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv3)


def reg_serv4(message):
    text = message.text
    text = text.split(", ")
    if len(text) == 3:
        Sqlighter.save_order("Подключение умного дома", text[0], text[1], text[2])
        bot.send_message(message.chat.id, "Ваш заказ успешно оформлен!")
        sticker = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sticker)

    elif message.text == "Поддержка ⚙️" or message.text == "Список услуг 📃" or message.text == "Напишите отзыв ✍️":
        bot.send_message(message.chat.id, "Отправьте сообщение еще раз")

    else:
        uncorrect = bot.send_message(message.chat.id, "Вы неправильно ввели данные, попробуйте снова")
        bot.register_next_step_handler(uncorrect, reg_serv4)


def review(message):
    if message.text != "Поддержка ⚙️" and message.text != "Список услуг 📃" and message.text != "Написать отзыв ✍️":
        Sqlighter.save_review(message.text)
        bot.send_message(message.chat.id, "Спасибо! отзывы помогут нам развиваться! 😁")

    else:
        bot.send_message(message.chat.id, "Нажмите еще раз.")


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


@bot.message_handler(content_types=["text"], chat_types=["private"])
def send_reply(message):
    if message.text == "Написать отзыв ✍️":
        sent = bot.send_message(message.chat.id, "Напишите отзыв ✍️")
        bot.register_next_step_handler(sent, review)

    elif message.text == "Список услуг 📃":
        photo = open("services.png", "rb")
        first = bot.send_photo(message.chat.id, photo, "Наши услуги")
        bot.register_next_step_handler(first, service_checker)

    elif message.text == "Поддержка ⚙️":
        url_but = types.InlineKeyboardMarkup(row_width=1)
        url_tg = types.InlineKeyboardButton("Связаться", url="https://t.me/GGAMID")
        url_but.add(url_tg)
        bot.send_message(message.chat.id, "Пишите на телеграмм ⤵️", reply_markup=url_but)

    elif message.text == "пароль: электрик - лучшая работа в мире":

        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        set_peregovorka = types.KeyboardButton("..Переговорка?..")
        about_salary = types.KeyboardButton("..INFO?..")
        info_but = types.KeyboardButton("⬅️COME BACK⬅️")
        kb.add(set_peregovorka, info_but, about_salary)
        bot.send_message(message.chat.id, "О! Привет, работник, ты попал в _секретную_ секцию! 🥷",parse_mode="markdown", reply_markup=kb)

    # elif message.text == "..Переговорка?..":
    #     inlineKb = types.InlineKeyboardMarkup(row_width=1)
    #     set_date = types.InlineKeyboardButton("Забронировать", callback_data="bron")
    #     when = types.InlineKeyboardButton("", callback_data="bron")

    elif message.text == "..INFO?..":
        bot.send_message(message.chat.id, f"*Ваша ЗП* = {Sqlighter.get_info_workers(message.chat.id)[0]}\n"
                                          f"*Дата ЗП* = {Sqlighter.get_info_workers(message.chat.id)[1]}\n"
                                          f"*Дата отпуска* = {Sqlighter.get_info_workers(message.chat.id)[2]}\n"
                                          f"*Дата на которую назначена переговорка* = {Sqlighter.get_info_workers(message.chat.id)[3]}", parse_mode="markdown")

    elif message.text == "⬅️COME BACK⬅️":

        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        get_list = types.KeyboardButton("Список услуг 📃")
        write_review = types.KeyboardButton("Написать отзыв ✍️")
        support = types.KeyboardButton("Поддержка ⚙️")
        kb.add(get_list, write_review, support)

        bot.send_message(message.chat.id, f"Клиентское меню", reply_markup=kb)

    else:
        bot.send_message("Я вас не понимаю :( ")

@bot.message_handler(commands=["start"], chat_types=["group"])
def sendler(message):
    bot.send_message(message.chat.id, f"Здравствуйте,"f"я бот компании *Электротехник*"
                                      f" и я буду следить за порядком в чате!", parse_mode="markdown",
                     reply_markup=None)


@bot.message_handler(content_types=["text"], chat_types=["group"])
def text_checkker(message):
    text = message.text
    if "мат" in text.lower():
        bot.send_message(message.chat.id, "не материтесь!")


def sendler_notification(salary, holiday, peregovorka):
    while True:
        for i in salary:
            bot.send_message(i, f"Скоро придет зарплата! 🎉 {Sqlighter.get_info_workers(i)[1]}")
        for i in holiday:
            bot.send_message(i, f"Скоро Отпуск! 🎉 {Sqlighter.get_info_workers(i)[2]}")
        for i in peregovorka:
            bot.send_message(i, f"Скоро перговоры! 🎉 {Sqlighter.get_info_workers(i)[3]}")
        time.sleep(86400)


th2 = Thread(target=sendler_notification,
             args=(sendler_notification_salary(get_data()), sendler_notification_holiday(get_data()), sendler_notification_peregovorka(get_data())))
th2.start()

th = Thread(target=bot.infinity_polling())
th.start()
