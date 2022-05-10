import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename).read()

# zip
import zipfile
zipfile.ZipFile(filename).read(filename)

# tar
import tarfile
tarfile.open(filename).read()

# rar
import rarfile
rarfile.RarFile(filename).read(filename)

# 7z
import py7zlib
py7zlib.Archive7z(open(filename)).getnames()

# PDF
import pyPdf
pdf = pyPdf.PdfFileReader(open(filename))
pdf.getDocumentInfo()
pdf.getNumPages()
pdf.getPage(0).extractText()

# Word
import docx
doc = docx.Document(filename)
doc.get_paragraphs()
doc.get_tables()

# Excel
import xlrd
xlrd.open_workbook(filename)

# PowerPoint
import pptx
pptx.Presentation(filename)

# Outlook
import olefile

