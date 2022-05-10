import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zf = zipfile.ZipFile(filename)
zf.open(zf.namelist()[0])

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.extractfile(tf.getnames()[0])

# csv
import csv
f = open(filename, 'rt')
reader = csv.reader(f)
for row in reader:
    print(row)

# json
import json
serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2014,
                  "topics" : [ "data", "science", "data science"] }"""

# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in des
