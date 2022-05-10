import lzma
lzma.open("xz_file.xz").read()

# bzip2
import bz2
bz2.open("bz2_file.bz2").read()

# gzip
import gzip
gzip.open("gz_file.gz").read()

# tar
import tarfile
tarfile.open("tar_file.tar").read()

# zip
import zipfile
zipfile.open("zip_file.zip").read()

# rar
import rarfile
rarfile.open("rar_file.rar").read()

# 7zip
import py7zlib
py7zlib.Archive7z("7z_file.7z").read()

# PDF
import pdfrw
pdfrw.PdfReader("pdf_file.pdf").read()

# Microsoft Office
import olefile
olefile.OleFileIO("ole_file.doc").read()

# OpenDocument
import olefile
olefile.OleFileIO("ole_file.odt").read()

# RTF
import ole
