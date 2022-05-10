import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'parking', 'parking', 'parking');

with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM vehicle")
    rows = cur.fetchall()
    for row in rows:
        print(row)
