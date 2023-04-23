import db
import export_files
import input_user
import modul
import view


def choice_acton(value):
    if value == 1:
        modul.create_note()
        view.head()
        choice_acton(view.get_value())
    elif value == 2:
        view.search_optons()
        search_action(view.get_value())
        view.head()
        choice_acton(view.get_value())
    elif value == 3:
        db.view_all_base()
        print("Выбирете заметку для редактирования(индекс): ")
        choice = view.get_value()
        view.update_options()
        update_index = view.get_value()
        update_data =  str(input("Введите новые данне: "))
        db.update_notes(choice,update_index,update_data)
        view.head()
        choice_acton(view.get_value())
    elif value == 4:
        db.view_all_base()
        choice = int(input("Выбирете заметку для удаления(индекс): "))
        db.del_notes(choice)
        view.head()
        choice_acton(view.get_value())
    elif value == 5:
        export_files.export_csv(5)
        print("Выгрузка завершенна успешно")
        view.head()
        choice_acton(view.get_value())
    elif value == 6:
        export_files.export_csv(6)
        print("Выгрузка завершенна успешно")
        view.head()
        choice_acton(view.get_value())
    elif value ==  7:
        db.view_all_base()
        view.head()
        choice_acton(view.get_value())
    elif value == 0:
        exit()



def search_action(value):
    if value == 1:
        db.search_notes(1,input_user.input_title())
    elif value == 2:
        db.search_notes(2,input_user.input_date())
    elif value == 3:
        db.search_notes(3,input_user.input_body())

