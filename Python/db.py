import mysql.connector
import  datetime
from mysql.connector import Error

def create_connect(host_name, user_name,user_passwd,db_name):
    connect = None
    try:
        connect = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_passwd,
            database = db_name
        )
    except Error as error:
        print(f"The error '{error}' ")
    return connect

def read_sql(connect, query):
    cursor = connect.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occured")

def save_notes(title,body,date):
    connect = create_connect("localhost","root","root","notes_python")
    sql = "INSERT INTO notes (title, body, date) VALUE (%s, %s, %s)"
    val =[(title,body,date)]
    cursor = connect.cursor()
    cursor.executemany(sql,val)
    connect.commit()
    print("Заметка записана")

def search_notes(index_search,data):
    connect = create_connect("localhost", "root", "root", "notes_python")
    date = str(data)
    if index_search == 1:
        select = f"SELECT * FROM notes WHERE title LIKE '%{date}%'"
    elif index_search ==2:
        select = f"SELECT * FROM notes WHERE date LIKE '%{date}%'"
    elif index_search == 3:
        select = f"SELECT * FROM notes WHERE body LIKE '%{date}%'"

    result = read_sql(connect,select)
    if len(result) == 0:
        print("Совпадение не найденны")
    else:
        for elements in result:
            index,note_title,note_body,note_date = elements
            print(f"Заголовок: {note_title}")
            print(f"Текс заметки: {note_body}")
            print(f"Дата заметки: {note_date}")

def view_all_base():
    connect = create_connect("localhost", "root", "root", "notes_python")
    select = "SELECT * FROM notes"
    result = read_sql(connect,select)
    for elements in result:
        index, note_title, note_body, note_date = elements
        print(f"Индекс: {index}")
        print(f"Заголовок: {note_title}")
        print(f"Текс заметки: {note_body}")
        print(f"Дата заметки: {note_date}")

def update_notes(index,update_index,update_date):
    connect = create_connect("localhost", "root", "root", "notes_python")
    if update_index == 1:
        select = f"UPDATE notes SET title = '{update_date}',date = '{datetime.datetime.now()}' WHERE ID = '{index}'"
    elif update_index == 2:
        select = f"UPDATE notes SET body = '{update_date}', date = '{datetime.datetime.now()}' WHERE ID = '{index}'"
    cursor = connect.cursor()
    try:
        cursor.execute(select)
        connect.commit()
        print("Запись успешно изменена")
    except Error as er:
        print(f"The error '{e}' occured")

def del_notes(index):
    connect = create_connect("localhost", "root", "root", "notes_python")
    select = f"DELETE FROM notes  WHERE ID =  '{index}'"
    cursor = connect.cursor()
    cursor.execute(select)
    connect.commit()
    print("Заметка успешно удаленна")

def export_base():
    connect = create_connect("localhost", "root", "root", "notes_python")
    select = "SELECT * FROM notes"
    result = read_sql(connect,select)
    return result


