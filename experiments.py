import time

month = int(time.strftime('%m', time.localtime()))
year = int(time.strftime('%Y', time.localtime()))
digit = int(time.strftime('%d', time.localtime()))


def sendler_notification_salary(list):
    month = int(time.strftime('%m', time.localtime()))
    year = int(time.strftime('%Y', time.localtime()))
    digit = int(time.strftime('%d', time.localtime()))
    a = []
    for i in list:
        date = list[i][1].split(".")
        if int(date[2]) == year:
            if month == int(date[1]) or month - int(date[1]) == -1:
                if int(date[0]) - digit == 3 or int(date[0]) - digit == 10 or int(date[0]) - digit == 0 or (
                        month - int(date[1]) == -1 and (
                        (int(date[0]) == 7 and digit == 27) or (int(date[0]) == 3 and (digit == 30 or digit == 31)))):
                    id = list[i][0]
                    a.append(id)
    return a


def sendler_notification_peregovorka(list):
    month = int(time.strftime('%m', time.localtime()))
    year = int(time.strftime('%Y', time.localtime()))
    digit = int(time.strftime('%d', time.localtime()))
    a = []
    for i in list:
        date = list[i][3].split(".")
        if int(date[2]) == year:
            if month == int(date[1]) or month - int(date[1]) == -1:
                if int(date[0]) - digit == 3 or int(date[0]) - digit == 10 or int(date[0]) - digit == 0 or (
                        month - int(date[1]) == -1 and (
                        (int(date[0]) == 7 and digit == 27) or (int(date[0]) == 3 and (digit == 30 or digit == 31)))):
                    id = list[i][0]
                    a.append(id)
    return a


def sendler_notification_holiday(list):
    month = int(time.strftime('%m', time.localtime()))
    year = int(time.strftime('%Y', time.localtime()))
    digit = int(time.strftime('%d', time.localtime()))
    a = []
    for i in list:
        date = list[i][2].split(".")
        if int(date[2]) == year:
            if month == int(date[1]) or month - int(date[1]) == -1:
                if int(date[0]) - digit == 3 or int(date[0]) - digit == 10 or int(date[0]) - digit == 0 or (month - int(date[1]) == -1 and ((int(date[0]) == 7 and digit == 27) or (int(date[0]) == 3 and (digit == 30 or digit == 31)))):
                    idshnik = list[i][0]
                    a.append(idshnik)
    return a

