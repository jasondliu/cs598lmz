import bz2
bz2.BZ2File(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# gzip
import gzip
gzip.GzipFile(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# tarfile
import tarfile
tarfile.TarFile(filename)

# rarfile
import rarfile
rarfile.RarFile(filename)

# 7zfile
import sevenzip
sevenzip.SevenZipFile(filename)

# warcio
import warcio
warcio.WARCFile(filename)

# lxml
import lxml
lxml.etree.parse(filename)

# xml.etree.ElementTree
import xml.etree.ElementTree
xml.etree.ElementTree.parse(filename)

# html5lib
import html5lib
html5lib.parse(filename)

# chardet
import chardet
chardet.detect(filename)

# cchardet
import cchardet
cchard
