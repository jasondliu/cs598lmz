import bz2
bz2.BZ2File(filename).read()

import gzip
gzip.open(filename, 'rb').read()

import lzma
lzma.open(filename).read()

import zipfile
zipfile.ZipFile(filename).read(filename)

import tarfile
tarfile.open(filename).extractall()

import csv
with open(filename) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        pass

import json
serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2014,
                  "topics" : [ "data", "science", "data science"] }"""

# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print(deserialized)

# round-trip back to JSON
end_result =
