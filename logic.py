import re
import datetime

from models import Person
from time_track import time_track


def create_db_table(args):
    Person.create_table()
    print('Table was created')


def create_record(args):
    birthday = datetime.datetime.strptime(args.date, "%d%m%Y").date()
    full_name = ' '.join(re.split('(?=[А-ЯA-Z])', args.full_name)[1:])
    gender = 'm' if args.gender == 'm' or args.gender == 'man' else 'w'
    Person.create(full_name=full_name, birthday=birthday, gender=gender)
    print(f'{full_name} added.')


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@time_track
def show_records(args):
    persons = Person.select(Person.full_name, Person.birthday).distinct().order_by(Person.full_name)
    for person in persons:
        age = calculate_age(person.birthday)
        print(person.full_name, person.birthday, age)
