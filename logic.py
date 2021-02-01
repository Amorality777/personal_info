import re
import datetime

from models import Person
from utils import calculate_age, birthday_generator, full_name_generator, full_name_start_with_f_generator, \
    create_records, time_track


def create_db_table(args):
    Person.create_table()
    print('Table was created')


def create_record(args):
    birthday = datetime.datetime.strptime(args.date, "%d%m%Y").date()
    full_name = ' '.join(re.split('(?=[А-ЯA-Z])', args.full_name)[1:])
    gender = 'm' if args.gender == 'm' or args.gender == 'man' else 'w'
    Person.create(full_name=full_name, birthday=birthday, gender=gender)
    print(f'{full_name} added.')


@time_track
def show_records(args):
    persons = Person.select(Person.full_name, Person.birthday).distinct().order_by(Person.full_name)
    for person in persons:
        age = calculate_age(person.birthday)
        print(person.full_name, person.birthday, age)


@time_track
def add_million_records(args):
    date_generator = birthday_generator()

    count_records = 10
    name_generator = full_name_generator()
    gender_list = ['m', 'w']
    create_records(count_records, date_generator, gender_list, name_generator)

    count_special_records = 100
    name_generator = full_name_start_with_f_generator()
    gender_list = ['m']
    create_records(count_special_records, date_generator, gender_list, name_generator)


@time_track
def show_selection_results(args):
    persons = Person.select().where((Person.full_name.startswith('F')) & (Person.gender == 'm')).order_by(
        Person.full_name)
    if persons:
        print(f'Total persons: {len(persons)}')
    else:
        print('No math')
