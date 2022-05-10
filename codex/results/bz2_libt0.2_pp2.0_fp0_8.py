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
zf.namelist()
zf.getinfo('file.txt')
zf.read('file.txt')

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.getnames()
tf.extractfile('file.txt')

# pickle
import pickle
pickle.dumps(obj)
pickle.loads(dumped_string)

# json
import json
json.dumps(obj)
json.loads(dumped_string)

# csv
import csv
with open(filename) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        pass

# xml
from xml.et
