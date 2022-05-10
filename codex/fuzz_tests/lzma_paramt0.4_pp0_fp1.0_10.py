from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
import zlib
zlib.decompress(data, -zlib.MAX_WBITS)

#%%
import bz2
bz2.decompress(data)

#%%
import lzma
lzma.decompress(data)

#%%
import zlib
import bz2
import lzma

uncompressed_data = zlib.decompress(data, -zlib.MAX_WBITS)
uncompressed_data = bz2.decompress(uncompressed_data)
uncompressed_data = lzma.decompress(uncompressed_data)
print(uncompressed_data)

#%%
import zlib
import bz2
import lzma

with open('lorem.txt', 'rb') as input:
    with lzma.open(input, 'rt') as decomp:
        text = decomp.read()
        print(text)

#%%
import zlib
import bz2
import lzma


