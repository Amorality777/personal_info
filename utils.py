import datetime
import time
from random import choice, randint, shuffle, sample

from models import Person

alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def full_name_generator():
    while True:
        full_name = ''
        for _ in range(3):
            full_name += choice(alphabet_upper)
            full_name += ''.join(sample(alphabet_lower, randint(2, 14))) + ' '
        yield full_name


print(next(full_name_generator()))


def full_name_start_with_f_generator():
    while True:
        full_name = ''
        for step in range(3):
            if step == 0:
                full_name += 'F'
            else:
                full_name += choice(alphabet_upper)
            full_name += ''.join(sample(alphabet_lower, randint(2, 14))) + ' '
        yield full_name.rstrip()


def birthday_generator():
    while True:
        day = randint(1, 28)
        month = randint(1, 12)
        year = randint(1950, 2020)
        yield datetime.date(year, month, day)


def create_records(count_records, date_generator, gender_list, name_generator):
    for _ in range(count_records):
        full_name = next(name_generator)
        birthday = next(date_generator)
        gender = choice(gender_list)
        Person.create(full_name=full_name, birthday=birthday, gender=gender)
    print(f'{count_records} records  created successfully')


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = ended_at - started_at
        time_result = f'{datetime.datetime.now()} -- Function {func.__name__} worked {elapsed:.4f} second(s)\n'
        print(time_result)
        with open('time_results.log', 'a') as f:
            f.write(time_result)
        return result

    return surrogate
