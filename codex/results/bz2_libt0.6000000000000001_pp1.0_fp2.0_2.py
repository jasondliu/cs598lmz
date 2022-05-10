import bz2
bz2.open('data.txt.bz2')

import gzip
gzip.open('data.txt.gz')

import zipfile
zipfile.open('data.zip')

# Reading data from the web
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)

# Parsing XML
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
root.tag
root.attrib
for child in root:
    print(child.tag, child.attrib)

# Parsing HTML
from lxml import html
tree = html.parse('data.html')
root = tree.getroot()
root.xpath('//a')
root.xpath('//a/@href')

# Interacting with databases
import sqlite3
conn
