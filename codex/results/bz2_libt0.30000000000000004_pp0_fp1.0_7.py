import bz2
bz2.BZ2File("data/sample.bz2").read()

import gzip
gzip.open("data/sample.gz").read()

import lzma
lzma.open("data/sample.xz").read()

import zipfile
z = zipfile.ZipFile("data/sample.zip")
z.extractall("data/")
z.close()

import tarfile
t = tarfile.open("data/sample.tar.gz")
t.extractall("data/")
t.close()

import csv
with open("data/sample.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import json
with open("data/sample.json") as f:
    data = json.load(f)
    print(data)

import xml.etree.ElementTree as et
tree = et.parse("data/sample.xml")
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.
