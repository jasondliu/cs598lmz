import bz2
bz2.open('data/sample.bz2')

# gzip
import gzip
gzip.open('data/sample.gz')

# lzma
import lzma
lzma.open('data/sample.xz')

# tar
import tarfile
tarfile.open('data/sample.tar')

# zip
import zipfile
zipfile.open('data/sample.zip')

# rar
import rarfile
rarfile.open('data/sample.rar')

# 7z
import py7zr
py7zr.SevenZipFile('data/sample.7z')

# pdf
import PyPDF2
PyPDF2.PdfFileReader('data/sample.pdf')

# doc
import docx
docx.Document('data/sample.docx')

# xls
import xlrd
xlrd.open_workbook('data/sample.xls')

# ppt
import pptx
pptx.Presentation('data/sample.pptx')

# mp3
import mutagen
mut
