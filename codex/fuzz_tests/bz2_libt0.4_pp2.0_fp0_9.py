import bz2
bz2.BZ2File(path)

#read a gzip file
import gzip
gzip.open(path)

#read a zip file
import zipfile
zipfile.ZipFile(path)

#read a pickle file
import pickle
pickle.load(path)

#read a json file
import json
json.load(path)

#read a csv file
import csv
csv.reader(path)

#read a text file
with open(path) as f:
    text = f.read()

#read a binary file
with open(path, 'rb') as f:
    binary = f.read()
    
#read a text file as a list of lines
with open(path) as f:
    lines = f.readlines()

#read a text file as a list of words
with open(path) as f:
    words = f.read().split()

#read a text file as a list of characters
with open(path) as f:
    chars = f.read().split()

#read a text file
