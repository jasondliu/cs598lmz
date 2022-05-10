from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
import bz2
bz2.decompress(data)

#%%
import zlib
zlib.decompress(data)

#%%
import lzma
lzma.decompress(data)

#%%
import lzma
lzma.decompress(data, format=lzma.FORMAT_RAW)

#%%
import lzma
lzma.decompress(data, format=lzma.FORMAT_XZ)

#%%
import lzma
lzma.decompress(data, format=lzma.FORMAT_ALONE)

#%%
import lzma
lzma.decompress(data, format=lzma.FORMAT_RAW, filters=[{'id': lzma.FILTER_LZMA2}])

#%%
import lzma
lzma.decompress(data, format=lzma.FORMAT_RAW, filters=[{'id': lzma.FILTER_LZ
