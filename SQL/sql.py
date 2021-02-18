import pyodbc
import config
from datetime import datetime
import time


class Database(object):
    def __init__(self):
        self.driver = 'DRIVER=' + config.DATABASE_DRIVER
        self.server = 'SERVER=' + config.DATABASE_URL
        self.port = 'PORT=' + config.DATABASE_PORT
        self.db = 'DATABASE=' + config.DATABASE_NAME
        self.user = 'UID=' + config.DATABASE_LOGIN
        self.pw = 'PWD=' + config.DATABASE_PASS
        self.conn_str = ';'.join([self.driver, self.server, self.port, self.db, self.user, self.pw])

    def db_connect(self):
        while True:
            try:
                self.connect = pyodbc.connect(self.conn_str)
                print(datetime.now().replace(microsecond=0), 'Connect OK')
                return self.connect
            except Exception as e:
                print(datetime.now().replace(microsecond=0), 'Error connect! Repeat after 60 seconds...')
                time.sleep(60)

    def connect_close(self):
        self.connect.close()
        print('Connect close!')


def sql_select(query):
    try:
        db = Database()
        cursor = db.db_connect().cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]    # Получаю список столбцов
        result = list()
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        db.connect_close()
        return result
    except Exception as e:
        raise e


def sql_uid(query, *params):
    try:
        db = Database()
        connect = db.db_connect()
        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()
        db.connect_close()
    except Exception as e:
        raise e




#users = sql_select('select * from Users')
#for user in users:
#    print(user)
#    print(user['id'])



