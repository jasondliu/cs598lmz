import bz2
bz2.BZ2File(filename)

#gzip
import gzip
gzip.open(filename, mode='rt')

#lzma
import lzma
lzma.open(filename)

#read a file
with open(filename) as f:
    lines = [x.rstrip() for x in f]

#write a file
with open(filename, 'w') as f:
    f.write(text)

#read a binary file
with open(filename, 'rb') as f:
    data = f.read()

#write a binary file
with open(filename, 'wb') as f:
    f.write(b'Hello World')

#structured file
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        pass

#json
import json
data = {
    'name' : 'ACME',
    'shares' : 100,
   
