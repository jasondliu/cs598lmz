import bz2
bz2.decompress(bz2.compress(b'hello world'))

import pickle
pickle.dumps(d)
pickle.loads(pickle.dumps(d))

import json
json.dumps(d)
json.loads(json.dumps(d))

import csv
f = open('mydata.csv', 'w')
writer = csv.writer(f)
writer.writerow(('number', 'number plus 2', 'number times 2'))
for i in range(10):
    writer.writerow((i, i+2, i*2))
f.close()

f = open('mydata.csv', 'r')
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

import sqlite3
conn = sqlite3.connect('database.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE people
(name TEXT, phone TEXT, email TEXT unique)''')
curs.execute('INSERT INTO people VALUES
