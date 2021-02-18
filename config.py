import os


def get_server_url():
    if os.environ.get('dev') == "true":
        return "localhost"
    else:
        return "10.128.0.2"


def get_server_driver():
    if os.environ.get('dev') == "true":
        return "SQL Server"
    else:
        return "ODBC Driver 17 for SQL Server"


DATABASE_URL = "85.175.4.154"
DATABASE_PORT = "1433"
DATABASE_NAME = "autotest_database"
DATABASE_LOGIN = "autotest_account"
DATABASE_PASS = "AutotestPass1"
DATABASE_DRIVER = "ODBC Driver 17 for SQL Server"

SERVER_URL = 'localhost'#get_server_url()
SERVER_PORT = 8080
