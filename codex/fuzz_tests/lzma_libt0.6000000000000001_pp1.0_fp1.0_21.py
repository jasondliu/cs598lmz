import lzma
lzma.open('test.lzma')

import bz2
bz2.open('test.bz2')

# OPENING GZIP FILES
import gzip
f = gzip.open('test.gz', 'wt')
f.write('lalala')
f.close()

import gzip
f = gzip.open('test.gz', 'rt')
text = f.read()
print(text)
f.close()

import gzip
with gzip.open('test.gz', 'wt') as f:
    f.write('lalala')

import gzip
with gzip.open('test.gz', 'rt') as f:
    text = f.read()
    print(text)

# OPENING ZIP ARCHIVES
import zipfile
with zipfile.ZipFile('test.zip') as zf:
    print(zf.namelist())

contents = zf.read('text.txt')

import zipfile
with zipfile.ZipFile('test.zip') as zf:
    for name
