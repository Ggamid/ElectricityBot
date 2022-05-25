import sqlite3


connect = sqlite3.connect("newBD.db")
cursor = connect.cursor()

class Sqlighter:

    def get_info(id):
        try:
            connect = sqlite3.connect("newBD.db")
            cursor = connect.cursor()

            info = cursor.execute("SELECT salary_sum, salary_date, holiday, peregovorka FROM workers WHERE id = ?", [id]).fetchone()
            return info


        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            connect.close()

