import sqlite3
from datetime import date  # Дата

connect = sqlite3.connect("newBD.db")
cursor = connect.cursor()
current_data = date.today()


class Sqlighter:

    def add_worker(Name, salary_sum, salary_date, holiday, peregovorka, id):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()
            info_list = (Name, salary_sum, salary_date, holiday, peregovorka, id)
            cursor.execute(
                "INSERT INTO workers (Name, salary_sum, salary_date, holiday, peregovorka, telegram_id) VALUES(?,?,?,?,?,?)",
                info_list)
            connect.commit()

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

    def get_info_workers(id):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            info = cursor.execute(
                "SELECT salary_sum, salary_date, holiday, peregovorka FROM workers WHERE telegram_id = ?",
                [id]).fetchone()
            return info


        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

    def check_id_customers(id):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            check = cursor.execute("SELECT id FROM reviews WHERE id = ?", [id]).fetchone()
            if check is None:
                return False
            else:
                return True
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

    def save_review(text):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            cursor.execute("INSERT INTO reviews(review, data) VALUES(?,?)", [text, current_data])
            connect.commit()
            print("Отзыв сохранен")


        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

    def save_order(phone_number, location, kind_order, data):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            listWthInfo = [kind_order, phone_number, location, data]

            cursor.execute("INSERT INTO order_table VALUES(?,?,?,?);", listWthInfo)
            connect.commit()
            return "Заказ с комментарием"
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

    def set_date_peregovorka(id, text1):
        try:

            date, ot, do = text1.split()[0], text1.split()[1], text1.split()[2]
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            cursor.execute("UPDATE workers SET peregovorka = ?, peregovorka_ot = ?, peregovorka_do = ? WHERE telegram_id = ?", [date, ot, do, id])
            connect.commit()
            return f"Переговорка заброниворона на {text1} число с {ot} и до {do} часов"
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()


def get_data():
    try:
        connect = sqlite3.connect("newBD.db")
        cursor = connect.cursor()

        first = cursor.execute("SELECT telegram_id, salary_date, holiday, peregovorka FROM workers").fetchall()

        second = {}
        for i in range(0, len(first)):
            second[i] = first[i]
        connect.commit()
        return second
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        connect.close()


def get_peregovorki():
    try:
        connect = sqlite3.connect("newBD.db")
        cursor = connect.cursor()

        first = cursor.execute("SELECT peregovorka, peregovorka_ot, peregovorka_do FROM workers").fetchall()

        second = []
        for i in first:
            second.append(i)
        connect.commit()
        return second
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        connect.close()


def check_peregovorki(stroka, listik):
    try:
        digit_p, month_p, year_p, ot, do = int(stroka.split()[0].split(".")[0]), int(stroka.split()[0].split(".")[1]), int(stroka.split()[0].split(".")[2]), int(stroka.split()[1]), int(stroka.split()[2])
        for i in range(0, len(listik)):
            if listik[i][0] == "":
                continue
            else:
                digit_listik, month_listik, year_listik = int(listik[i][0].split(".")[0]), int(listik[i][0].split(".")[1]), int(listik[i][0].split(".")[2])
                ot_listik, do_listik = int(listik[i][-2]), int(listik[i][-1])
                if year_listik == year_p:
                    if month_p == month_listik:
                        if digit_listik == digit_p:
                            if (ot_listik == ot) or (ot_listik < ot < do_listik) or (ot_listik < do < do_listik) or (do == do_listik) or (ot < ot_listik < do):
                                return "На это время переговорка занята"
                            else:
                                return True
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
        return True
    except:
        print("Error in check peregovorki")


