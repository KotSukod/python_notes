def head():
    print(" ")
    print("1 - Создать заметку")
    print("2 - Найти заметку")
    print("3 - Редактирование заметки")
    print("4 - Удаление заметки")
    print("5 - Сохранить в csv")
    print("6 - Сохранить в json")
    print("7 - Показать весь список заметок")
    print("0 - Выход")
def get_value ():
   return int(input("=> "))

def search_optons():
    print(" ")
    print("1 - По заголовку")
    print("2 - По дате")
    print("3 - По тексту")

def update_options():
    print(" ")
    print("Какое поле нужно отредактировать?")
    print("1 - Заголовок")
    print("2 - Текст")
