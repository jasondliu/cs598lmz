import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

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

# pickle
import pickle
pickle.load(open(filename, 'rb'))

# json
import json
json.load(open(filename, 'rb'))

# csv
import csv
csv.reader(open(filename, 'rb'))

# xls
import xlrd
book = xlrd.open_workbook(filename)
book.sheet_names()
sheet = book.sheet_by_name(sheet_name)
sheet.row_values(0)
sheet.col_values(0)
sheet.cell(0, 0).value

# sqlite
import sqlite3
