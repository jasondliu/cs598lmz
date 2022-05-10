import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
zipfile.ZipFile(filename)

import tarfile
tarfile.TarFile(filename)

import csv
csv.reader(filename)

import sqlite3
conn = sqlite3.connect(filename)

import json
json.load(filename)

import pickle
pickle.load(filename)

import shelve
shelve.open(filename)

import xmlrpc.client
proxy = xmlrpc.client.ServerProxy(filename)

import email
email.message_from_file(filename)

import html
html.parse(filename)

import cgi
cgi.parse(filename)

import xml.etree.ElementTree
xml.etree.ElementTree.parse(filename)

import xml.dom.minidom
xml.dom.minidom.parse(filename)

import xml.sax
xml.sax.parse(
