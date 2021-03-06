import argparse

from logic import create_db_table, create_record, show_records, add_million_records, show_selection_results

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

create_parser = subparsers.add_parser('1', help='create table')
create_parser.set_defaults(func=create_db_table)

add_parser = subparsers.add_parser('2', help='add person')
add_parser.add_argument('full_name', action="store")
add_parser.add_argument('date', action="store", help='format ddmmYYYY')
add_parser.add_argument('gender', action="store", choices=['m', 'man', 'w', 'woman'])
add_parser.set_defaults(func=create_record)

show_parser = subparsers.add_parser('3', help='show records')
show_parser.set_defaults(func=show_records)

show_parser = subparsers.add_parser('4', help='add million records')
show_parser.set_defaults(func=add_million_records)

show_parser = subparsers.add_parser('5', help='selection results')
show_parser.set_defaults(func=show_selection_results)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
