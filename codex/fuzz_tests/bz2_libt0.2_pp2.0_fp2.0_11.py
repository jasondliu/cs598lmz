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
zf.extractall(path='.')

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.extractall(path='.')

# pickle
import pickle
pkl_file = open(filename, 'rb')
data1 = pickle.load(pkl_file)
pkl_file.close()

# json
import json
json_file = open(filename, mode='r')
data = json.load(json_file)
json_file.close()

# csv
import csv
with open(filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        print(', '.
