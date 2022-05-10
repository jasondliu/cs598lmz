import bz2
bz2.BZ2File('data/example.bz2')

# gzip
import gzip
f = gzip.open('data/example.gz', 'rb')
f.read()

# zip
import zipfile
z = zipfile.ZipFile('data/example.zip', 'r')
z.extractall('data/example')

# tar
import tarfile
t = tarfile.open('data/example.tar.gz', 'r:gz')
t.extractall('data/example')

# csv
import csv
f = open('data/example.csv')
reader = csv.reader(f)
for line in reader:
    print(line)

# json
import json
path = 'data/example.json'
records = [json.loads(line) for line in open(path, 'rb')]
records[0]

# xml
from lxml.html import parse
from urllib2 import urlopen
parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=
