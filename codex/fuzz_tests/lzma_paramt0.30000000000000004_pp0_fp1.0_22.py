from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%

import lzma

with lzma.open('foo.xz', 'rt') as f:
    file_content = f.read()

#%%

import lzma

with lzma.open('foo.xz', 'wt') as f:
    f.write(file_content)

#%%

import lzma

with lzma.open('foo.xz', 'wt') as f:
    f.write(file_content)

#%%

import lzma

with lzma.open('foo.xz', 'wt') as f:
    f.write(file_content)

#%%

import lzma

with lzma.open('foo.xz', 'wt') as f:
    f.write(file_content)

#%%

import lzma

with lzma.open('foo.xz', 'wt') as f:
    f.write(file_content)

#%%

import lz
