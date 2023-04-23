import datetime

import db
import input_user
from datetime import date


def create_note():
    title = input_user.input_title()
    note_body = input_user.input_body()
    note_date = datetime.datetime.now()
    db.save_notes(title,note_body,note_date)

def search_note(data,index):
    if index == 1:
        db.search_notes(1,data)







