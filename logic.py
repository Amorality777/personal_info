import re
import datetime

from models import Person, Gender
from utils import calculate_age, birthday_generator, full_name_generator, full_name_start_with_f_generator, \
    create_records, time_track


def create_db_table(args):
    Person.create_table()
    Gender.create_table()
    Gender.create(gender='m')
    Gender.create(gender='w')
    print('Table was created')


def create_record(args):
    birthday = datetime.datetime.strptime(args.date, "%d%m%Y").date()
    full_name = ' '.join(re.split('(?=[А-ЯA-Z])', args.full_name)[1:])
    gender = Gender.get_by_id(1) if args.gender == 'm' or args.gender == 'man' else Gender.get_by_id(2)
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

    count_records = 1000
    name_generator = full_name_generator()
    gender_list = [Gender.get_by_id(1), Gender.get_by_id(2)]
    create_records(count_records, date_generator, gender_list, name_generator)

    count_special_records = 100
    name_generator = full_name_start_with_f_generator()
    gender_list = [Gender.get_by_id(1)]
    create_records(count_special_records, date_generator, gender_list, name_generator)


@time_track
def show_selection_results(args):
    persons = Person.select().order_by(Person.full_name).where(
        (Person.full_name.startswith('F')) & (Person.gender == Gender.get_by_id(1)))
    if persons:
        print(f'Total persons: {len(persons)}')
    else:
        print('No math')
