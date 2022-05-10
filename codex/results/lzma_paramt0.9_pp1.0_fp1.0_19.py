from lzma import LZMADecompressor
LZMADecompressor().decompress(array)

#%%
import gzip
gzip.decompress(array)

#%%
import bz2
bz2.decompress(array)

#%%
import zlib

zlib.decompress(array)

#%%
