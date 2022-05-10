from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%

import lzma
with lzma.open('data/data.xz', 'rb') as f:
    file_content = f.read()

#%%

import bz2
with bz2.open('data/data.bz2', 'rt') as f:
    file_content = f.read()

#%%

import bz2
with bz2.open('data/data.bz2', 'rt') as f:
    file_content = f.read()

#%%

import gzip
with gzip.open('data/data.gz', 'rt') as f:
    file_content = f.read()

#%%

import gzip
with gzip.open('data/data.gz', 'rt') as f:
    file_content = f.read()

#%%

import gzip
with gzip.open('data/data.gz', 'rt') as f:
    file_content = f.read()

#%%

import gzip

