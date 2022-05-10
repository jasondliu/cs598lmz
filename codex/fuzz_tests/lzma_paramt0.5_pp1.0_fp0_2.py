from lzma import LZMADecompressor
LZMADecompressor.decompress(f.read())

#%%
import bz2
bz2.decompress(f.read())

#%%
import gzip
gzip.decompress(f.read())

#%%
import zlib
zlib.decompress(f.read())

#%%
import lzma
lzma.decompress(f.read())

#%%
import zlib
import gzip
import bz2
import lzma
import sys

#%%
def compress(data, mode):
    """Compress data using the specified mode."""
    if mode == 'zlib':
        return zlib.compress(data)
    elif mode == 'gzip':
        return gzip.compress(data)
    elif mode == 'bz2':
        return bz2.compress(data)
    elif mode == 'lzma':
        return lzma.compress(data)
    else:
        return data

def decompress(data, mode):
    """Decompress data using the
