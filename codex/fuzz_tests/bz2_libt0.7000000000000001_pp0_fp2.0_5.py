import bz2
bz2.compress(b"hello world")

import lzma
lzma.compress(b"hello world")
import csv
csv.reader(open("test.csv"))

with open("test.csv") as f:
    for row in csv.reader(f):
        print(row)

with open("test.csv") as f:
    for row in csv.DictReader(f):
        print(row)
import urllib.request
urllib.request.urlopen("https://www.python.org")

import xml.etree.ElementTree as etree
tree = etree.parse("test.xml")
root = tree.getroot()
root.tag
for child in root:
    print(child.tag, child.attrib)

root[0][1].text

tree.findall("./user")
tree.findall("./user/age")
tree.findall(".//age")

tree.findall(".//age")[0].text

for user in tree.findall("./
