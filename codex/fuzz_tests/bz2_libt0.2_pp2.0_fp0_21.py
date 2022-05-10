import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# pickle
import pickle
pickle.load(file)

# json
import json
json.load(file)

# csv
import csv
csv.reader(file)

# xml
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# html
import lxml.html
tree = lxml.html.parse(filename)
root = tree.getroot()

# excel
import openpyxl
wb = openpyxl.load_workbook(filename)

# pdf
import PyPDF2
pdf = PyPDF2.PdfFileReader(file)

# word
import docx
doc = docx.
