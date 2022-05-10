import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# tar
import tarfile
tar = tarfile.open(filename)
tar.extractall()
tar.close()

# zip
import zipfile
zip = zipfile.ZipFile(filename)
zip.extractall()
zip.close()

# json
import json
json.load(open(filename))

# csv
import csv
f = open(filename, 'r')
csvreader = csv.reader(f)
for row in csvreader:
    print(row)
f.close()

# xml
from xml.etree.ElementTree import parse
doc = parse(filename)

# html
from urllib.request import urlopen
from bs4 import BeautifulSoup
text = urlopen(url).read()
soup = BeautifulSoup(text, 'html.parser')

# binary data
import struct
with
