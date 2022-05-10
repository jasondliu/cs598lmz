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
pickle.load(filename)

# json
import json
json.load(filename)

# csv
import csv
csv.reader(filename)

# xml
import xml.etree.ElementTree as et
et.parse(filename)

# html
from bs4 import BeautifulSoup
soup = BeautifulSoup(filename, 'html.parser')

# excel
import openpyxl
wb = openpyxl.load_workbook(filename)

# pdf
import PyPDF2
pdf = PyPDF2.PdfFileReader(filename)
