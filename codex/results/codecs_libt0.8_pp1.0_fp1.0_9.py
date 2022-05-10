import codecs
codecs.register(lambda name: name == 'cp65001' and
                codecs.lookup('utf-8') or None)

from db import db_session, init_db
from models import User, Account, Book, AccountBook

"""
python -m data_import.import_book <book_file>
python -m data_import.import_book ../../data/book_info.csv
"""

if __name__ == '__main__':
    if db_session is None:
        init_db()

    with open(sys.argv[1]) as book_info_file:
        reader = csv.DictReader(book_info_file, delimiter=',', quotechar='"')
        for row in reader:
            isbn = row['isbn'].strip().replace('-', '')
            if isbn == '' or Book.query.filter(Book._isbn == isbn).first() is not None:
                continue

            authors = row['authors'].split('/')
            for author in authors:
                author = author.strip()

           
