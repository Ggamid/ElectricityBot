import sqlite3
from datetime import date # Дата
import datetime
connect = sqlite3.connect("newBD.db")
cursor = connect.cursor()
current_data = date.today()


class Sqlighter:

    def get_info_workers(id):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            info = cursor.execute("SELECT salary_sum, salary_date, holiday, peregovorka FROM workers WHERE id = ?",
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




