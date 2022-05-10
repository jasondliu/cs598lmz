import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.TarFile(filename)

# rar
import rarfile
rarfile.RarFile(filename)

# 7z
import py7zlib
py7zlib.Archive7z(filename)

# csv
import csv
csv.reader(filename)

# json
import json
json.load(filename)

# xml
import xml.etree.ElementTree as ET
ET.parse(filename)

# yaml
import yaml
yaml.load(filename)

# pdf
import PyPDF2
PyPDF2.PdfFileReader(filename)

# docx
import docx
docx.Document(filename)

# xlsx
import xlrd
xlrd.open_workbook(filename)


