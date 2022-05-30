import time
import telebot
from BotToken import token
from workWithDB import Sqlighter
from telebot import types
from threading import Thread
from experiments import sendler_notification_holiday, sendler_notification_peregovorka, sendler_notification_salary
from workWithDB import get_data, check_peregovorki, get_peregovorki

kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
get_list = types.KeyboardButton("Список услуг 📃")
write_review = types.KeyboardButton("Написать отзыв ✍️")
support = types.KeyboardButton("Поддержка ⚙️")
kb.add(get_list, write_review, support)

kb_undo = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
undo = types.KeyboardButton("Отмена ❌")
kb_undo.add(undo)

kb_special = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
set_peregovorka = types.KeyboardButton("..Переговорка?..")
about_salary = types.KeyboardButton("..INFO?..")
info_but = types.KeyboardButton("⬅️COME BACK⬅️")
kb_special.add(set_peregovorka, info_but, about_salary)

sticker = open("sticker.webp", "rb")


def match_reg_serv(mes):
    text = mes.text
    text = text.split(", ")
    kind_of_serv = text[0]
    if len(text) == 4:
        match kind_of_serv:
            case "1":

                Sqlighter.save_order("Провести электричество в дом", text[1], text[2], text[3])
                bot.send_message(mes.chat.id,
                                 "✅ Заказ оформлен на услугу 'Провести электричество в дом'"
                                 , reply_markup=kb)

            case "2":

                Sqlighter.save_order("Дизайнерские лампы для вашего дома", text[1], text[2], text[3])
                bot.send_message(mes.chat.id,
                                 "✅ Заказ оформлен на услугу 'Дизайнерские лампы для вашего дома"
                                 , reply_markup=kb)

            case "3":

                Sqlighter.save_order("Установка кондиционеров", text[1], text[2], text[3])
                bot.send_message(mes.chat.id,
                                 "✅ Заказ оформлен на услугу 'Установка кондиционеров"
                                 , reply_markup=kb)

            case "4":

                Sqlighter.save_order("Подключение умного дома", text[1], text[2], text[3])
                bot.send_message(mes.chat.id,
                                 "✅ Заказ оформлен на услугу 'Подключение умного дома"
                                 , reply_markup=kb)
            case _:
                send_reply(mes)
    elif mes.text == "Отмена ❌":
        send_reply(mes)
    else:
        wrong = bot.send_message(mes.chat.id, "Не правильно введены данные")
        bot.register_next_step_handler(wrong, match_reg_serv)


def set_pere(message):
    if check_peregovorki(message.text, get_peregovorki()) == 1:
        bot.send_message(message.chat.id, Sqlighter.set_date_peregovorka(message.chat.id, message.text))
        bot.send_sticker(message.chat.id, sticker)

    elif check_peregovorki(message.text, get_peregovorki()) == "На это время переговорка занята":
        bot.send_message(message.chat.id, "На это время переговорка занята, выберете другую дату", reply_markup=kb_undo)
    else:
        send_reply(message)


def review(message):
    if message.text != "Поддержка ⚙️" and message.text != "Список услуг 📃" and message.text != "Написать отзыв ✍️" and message.text != "Отмена ❌":
        Sqlighter.save_review(message.text)

        bot.send_message(message.chat.id, "Спасибо! отзывы помогут нам развиваться! 😁", reply_markup=kb)
        bot.send_sticker(message.chat.id, sticker)

    else:
        send_reply(message)

#1791379170
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"], chat_types=["private"])
def sendler(message):
    if Sqlighter.get_info_workers(message.from_user.id) is None:

        bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}, "
                                          f"я бот компании *Электротехник*"
                         , parse_mode="markdown", reply_markup=kb)
        print(message.chat.id)
    else:
        bot.send_message(message.chat.id, "HI worker", reply_markup=kb)
        print(message.chat.id)


@bot.message_handler(content_types=["text"], chat_types=["private"])
def send_reply(message):
    if message.text == "Написать отзыв ✍️":
        sent = bot.send_message(message.chat.id, "Напишите отзыв ✍️", reply_markup=kb_undo)
        bot.register_next_step_handler(sent, review)

    elif message.text == "Список услуг 📃":
        photo = open("services.png", "rb")
        first = bot.send_photo(message.chat.id, photo,
                               "Чтобы оформить услугу отправьте через запятую номер услуги, ваш номер телефона, адрес проживания, и дату на которую хотите заказать услугу. \n Пример: \n"
                               "1, 89992576336, Улица Пушкина дом 4 квартира 25, 01.06.2022", reply_markup=kb_undo)
        bot.register_next_step_handler(first, match_reg_serv)

    elif message.text == "Поддержка ⚙️":
        url_but = types.InlineKeyboardMarkup(row_width=1)
        url_tg = types.InlineKeyboardButton("Связаться", url="https://t.me/GGAMID")
        url_but.add(url_tg)
        bot.send_message(message.chat.id, "Пишите на телеграмм ⤵️", reply_markup=url_but)

    elif message.text == "пароль: электрик - лучшая работа в мире":

        bot.send_message(message.chat.id, "О! Привет, работник, ты попал в _секретную_ секцию! 🥷",
                         parse_mode="markdown", reply_markup=kb_special)

    elif message.text == "..Переговорка?..":
        nexter = bot.send_message(message.chat.id,
                                  "Отправьте дату на которую хотите забронировать переговорку в формате:\n"
                                  "22.02.2022 15 16\n"
                                  "(последние две цифры - со скольки и до скольки часов", reply_markup=kb_undo)
        bot.register_next_step_handler(nexter, set_pere)

    elif message.text == "..INFO?..":
        bot.send_message(message.chat.id, f"*Ваша ЗП* = {Sqlighter.get_info_workers(message.chat.id)[0]}\n"
                                          f"*Дата ЗП* = {Sqlighter.get_info_workers(message.chat.id)[1]}\n"
                                          f"*Дата отпуска* = {Sqlighter.get_info_workers(message.chat.id)[2]}\n"
                                          f"*Дата на которую назначена переговорка* = {Sqlighter.get_info_workers(message.chat.id)[3]}",
                         parse_mode="markdown")


    elif message.text == "⬅️COME BACK⬅️":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        get_list = types.KeyboardButton("Список услуг 📃")
        write_review = types.KeyboardButton("Написать отзыв ✍️")
        support = types.KeyboardButton("Поддержка ⚙️")
        kb.add(get_list, write_review, support)

        bot.send_message(message.chat.id, f"Клиентское меню", reply_markup=kb)
    elif message.text == "Отмена ❌":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        get_list = types.KeyboardButton("Список услуг 📃")
        write_review = types.KeyboardButton("Написать отзыв ✍️")
        support = types.KeyboardButton("Поддержка ⚙️")
        kb.add(get_list, write_review, support)

        bot.send_message(message.chat.id, f"Главное меню", reply_markup=kb)


    else:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        get_list = types.KeyboardButton("Список услуг 📃")
        write_review = types.KeyboardButton("Написать отзыв ✍️")
        support = types.KeyboardButton("Поддержка ⚙️")
        kb.add(get_list, write_review, support)
        bot.send_message(message.chat.id, "Я вас не понимаю :( ", reply_markup=kb)


@bot.message_handler(commands=["start"], chat_types=["group"])
def sendler(message):
    bot.send_message(message.chat.id, f"Всем привет! Я бот компании *Электротехник*"
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
        if type(peregovorka) != bool:
            for i in peregovorka:
                bot.send_message(i, f"Скоро перговоры! 🎉 {Sqlighter.get_info_workers(i)[3]}")
        time.sleep(86400)


th2 = Thread(target=sendler_notification,
             args=(sendler_notification_salary(get_data()), sendler_notification_holiday(get_data()),
                   sendler_notification_peregovorka(get_data())))
th2.start()

th = Thread(target=bot.infinity_polling())
th.start()
