from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# (a)

# (b)
import csv
with open('data/presidents.csv', newline='') as f:
    for row in csv.reader(f):
        print(row)

# (c)
with open('data/presidents.csv', newline='') as f:
    for row in csv.DictReader(f):
        print(row['lastname'], row['firstname'])

# (d)
import json
with open('data/presidents.json') as f:
    presidents = json.load(f)

# (e)
with open('data/presidents.json') as f:
    presidents = json.load(f)
    presidents.sort(key=lambda president: president['start'])
