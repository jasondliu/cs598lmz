import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(filename)

# csv
import csv
csv.reader(open(filename))

# json
import json
json.load(open(filename))

# xml
import xml.etree.ElementTree as etree
etree.parse(filename)

# html
from bs4 import BeautifulSoup
soup = BeautifulSoup(open(filename), 'html.parser')

# excel
import pandas
xls = pandas.ExcelFile(filename)
xls.parse(sheet_name)

# sql
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute('select * from mytable')
curs.fetchall()

# pdf

