import bz2
bz2_file = bz2.BZ2File('file.bz2')
print bz2_file.readline().strip()
print bz2_file.readline()
bz2_file.seek(15)
bz2_file.readline()

with bz2.BZ2File('data.csv.bz2') as bz2_file:
    for line in bz2_file:
        # do stuff
        pass

import gzip
with gzip.GzipFile('data.csv.gz') as gz_file:
    for line in gz_file:
        # do stuff
        pass

import os
os.remove('file.txt')
