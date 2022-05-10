import bz2
bz2.BZ2File(filename)

import pickle
pickle.load(open(filename, 'rb'))

import json
json.load(open(filename, 'r'))

import csv
csv.reader(open(filename, 'rb'))

import zipfile
zipfile.ZipFile(filename)

import h5py
h5py.File(filename)

import pandas
pandas.read_csv(filename)

import sqlite3
conn = sqlite3.connect(filename)

import lxml.html
lxml.html.parse(filename)

import requests
r = requests.get(filename)

import BeautifulSoup
BeautifulSoup.BeautifulSoup(open(filename, 'r'))

import xml.etree.ElementTree
xml.etree.ElementTree.parse(filename)
