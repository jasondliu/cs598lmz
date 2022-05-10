import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sqlite3

def main():
    conn = sqlite3.connect('../../../data/sqlite3/tweets.db')
    c = conn.cursor()
    c.execute("select id, text, created_at from tweets")
    for row in c:
        print(row)


if __name__ == '__main__':
    main()
