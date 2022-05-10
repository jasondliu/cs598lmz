import bz2
bz2.BZ2File('data.txt.bz2')

import gzip
gzip.open('data.txt.gz')

import lzma
lzma.LZMAFile('data.txt.xz')

with bz2.open('data.txt.bz2', 'rt') as f:
    for line in f:
        print(line)

with gzip.open('data.txt.gz', 'rt') as f:
    for line in f:
        print(line)

with lzma.open('data.txt.xz', 'rt') as f:
    for line in f:
        print(line)

import shutil
with gzip.open('data.txt.gz', 'rt') as f_in:
    with open('data.txt', 'wt') as f_out:
        shutil.copyfileobj(f_in, f_out)
