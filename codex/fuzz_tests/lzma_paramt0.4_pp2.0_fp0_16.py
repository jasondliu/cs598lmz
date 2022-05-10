from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
import lzma
with lzma.open("data.xz") as f:
    file_content = f.read()

#%%
import bz2
with bz2.open("data.bz2") as f:
    file_content = f.read()

#%%
import gzip
with gzip.open("data.gz") as f:
    file_content = f.read()

#%%
import zlib
with open("data.zlib", "rb") as f:
    file_content = f.read()

#%%
import zlib
with open("data.zlib", "rb") as f:
    file_content = f.read()
    decompressed_data = zlib.decompress(file_content)

#%%
import zlib
with open("data.zlib", "rb") as f:
    file_content = f.read()
    decompressor = zlib.decompressobj()
    decompressed_data = decompressor.decompress(file_
