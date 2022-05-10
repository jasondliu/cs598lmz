import bz2
bz2_file = bz2.BZ2File('data/data.bz2')
data = bz2_file.read()
print(data)

# gzip
import gzip
gzip_file = gzip.GzipFile('data/data.gz')
data = gzip_file.read()
print(data)

# zip
import zipfile
z = zipfile.ZipFile('data/data.zip')
print(z.read('data/data.txt'))

# tar
import tarfile
t = tarfile.TarFile('data/data.tar')
print(t.getmembers())
print(t.extractfile('data/data.txt').read())

# csv
import csv
with open('data/data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# json
import json
with open('data/data.json') as f:
    data = json.load(f)
print(data)

# excel
import openpyxl
