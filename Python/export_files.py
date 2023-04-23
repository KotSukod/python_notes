import db


def export_csv(index_file):
    base = db.export_base()
    if index_file == 5:
        file_open = 'notes.csv'
    elif index_file == 6:
        file_open = 'notes.json'

    with open(file_open, 'w') as file:
        file.write('{};{};{};{}\n'.format("Индекс","Заголовок","Текст заметки","Дата"))
        index = 1
        for elements in base:
            index, note_title, note_body, note_date = elements
            file.write('{};{};{};{}\n'.format(index,note_title,note_body,note_date))
            index += 1