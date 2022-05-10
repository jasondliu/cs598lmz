from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#%%
import bz2, lzma
bz2.decompress(data)
lzma.decompress(data)

#%%
import gzip
with gzip.open('sample.txt.gz', 'rt') as f:
    text = f.read()

#%%
with gzip.open('sample.txt.gz', 'wt') as f:
    f.write(text)

#%%
import bz2
with bz2.open('sample.txt.bz2', 'rt') as f:
    text = f.read()

#%%
with bz2.open('sample.txt.bz2', 'wt') as f:
    f.write(text)

#%%
import lzma
with lzma.open('sample.txt.xz', 'rt') as f:
    text = f.read()

#%%
with lzma.open('sample.txt.xz', 'wt') as f:
    f.write(text)

#%%
