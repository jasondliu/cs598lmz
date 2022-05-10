from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
import gzip
import io

with gzip.open('somefile.gz', 'rb') as f:
    file_content = f.read()

#%%
file_content = gzip.decompress(data)

#%%
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

#%%
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

#%%
import bz2

with bz2.open('somefile.bz2', 'rt') as f:
    file_content = f.read()

#%%
file_content = bz2.decompress(data)

#%%
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

#%%
with bz2.open('somefile.bz2', 'wt', compresslevel=9) as f:
    f
