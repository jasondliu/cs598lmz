from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('workfile', 'rb').read())

# File-like Objects
f = open('workfile', 'rb')
f.read(size)
f.seek(offset, from_what)
f.write(b'abc')
f.tell()
f.close()

# Safely Reading and Writing Files
f = open('workfile', 'w')
try:
    f.write('This is a test\n')
finally:
    f.close()

with open('workfile') as f:
    read_data = f.read()

f.closed

# Saving Structured Data with json
import json
json.dumps([1, 'simple', 'list'])

with open('some_file', 'w') as f:
    json.dump(x, f)

with open('some_file') as f:
    x = json.load(f)

# Reading and Writing CSV Data
import csv
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect='
