import bz2
bz2.BZ2File('example.bz2').read()

# gzip
import gzip
gzip.GzipFile('example.gz').read()

# lzma
import lzma
lzma.LZMAFile('example.xz').read()

# zip
import zipfile
zipfile.ZipFile('example.zip').read('README.txt')

# tar
import tarfile
tarfile.open('example.tar.gz').read()

# pickle
import pickle
pickle.dumps([1, 2, 3, 4])

# json
import json
json.dumps([1, 2, 3, 4])

# csv
import csv
with open('example.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i + 2, i * 2))

# xml
import xml.etree.ElementTree as ET

