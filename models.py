from peewee import *

db = SqliteDatabase('db.sqlite3')


class Gender(Model):
    GENDER_CHOICES = [
        ('m', 'Man'),
        ('w', 'Woman'),
    ]
    gender = CharField(choices=GENDER_CHOICES)

    class Meta:
        database = db


class Person(Model):
    full_name = TextField()
    birthday = DateField()
    gender = ForeignKeyField(Gender)

    class Meta:
        database = db
        order_by = ['full_name']
