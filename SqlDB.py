import sqlite3

class SqlDB:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, user_name ="None"):
        with self.connection:
            self.cursor.execute('INSERT INTO users (user_id, user_name) VALUES(?,?)', (user_id, user_name)).fetchall()

    def get_users_name(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT user_name FROM users WHERE user_id = ?', (user_id,)).fetchall()
            return result


    def change_users_name(self, user_id, user_name):
        with self.connection:
            result = self.cursor.execute('UPDATE users SET user_name = ? WHERE user_id = ?', (user_name, user_id,)).fetchall()
            return result

    def check_user(self, id_to_check):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (id_to_check,)).fetchall()
            return bool(len(result))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()