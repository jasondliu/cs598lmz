import bz2
bz2.BZ2File('../data/sample.bz2')

import gzip
gzip.open('../data/sample.gz')

import lzma
lzma.open('../data/sample.xz')

import zipfile
zipfile.ZipFile('../data/sample.zip')

import tarfile
tarfile.open('../data/sample.tar')

# Dealing with HTML
import html5lib
html5lib.parse('<html><head><title>Title</title></head></html>')

import lxml.etree
lxml.etree.parse('<html><head><title>Title</title></head></html>')

import bs4
bs4.BeautifulSoup('<html><head><title>Title</title></head></html>')

import html.parser
html.parser.HTMLParser().parse('<html><head><title>Title</title></head></html>')

# Dealing with CSV
import csv
csv.reader(open('../data/sample.csv'))

import pandas as p
