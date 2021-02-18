from SQL.sql import sql_uid, sql_select


def login(username, password):
    sql_query = "select * from dbo.Users where login = '{login}' and password = '{password}'"
    result = sql_select(sql_query.format(login=username, password=password))
    print(result)
    if len(result) > 0:
        return"Добро пожаловать, {front_name}!".format(front_name=result[0]["front_name"])
    else:
        return "Неверный логин/пароль"


def reg(username, password, front_name):
    sql_query = "INSERT INTO dbo.Users (login, password, front_name) VALUES (?, ?, ?)"
    try:
        sql_uid(sql_query, username, password, front_name)
        return "Аккаунт зарегистрирован!"
    except Exception as e:
        sqlstate = e.args[0]
        if sqlstate == "23000":
            return "Данный логин уже зарегистрирован"
        elif sqlstate == "42000":
            return "Некорректные данные"
        else:
            return "Ошибка регистрации: {error}".format(error=str(sqlstate))
