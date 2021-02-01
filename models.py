from peewee import *
from datetime import date

db = SqliteDatabase('db.sqlite3')


class Person(Model):
    GENDER_CHOICES = [
        ('m', 'Man'),
        ('w', 'Woman'),
    ]
    full_name = TextField()
    birthday = DateField()
    gender = CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        database = db
        order_by = ['full_name']


