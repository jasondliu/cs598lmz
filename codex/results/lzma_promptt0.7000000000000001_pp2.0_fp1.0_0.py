import lzma
# Test LZMADecompressor on the generated data

with lzma.open("lzma_compressed", "rb") as f:
    data = f.read()
    
    with lzma.open("lzma_decompressed", "wb") as g:
        g.write(data)
 
# Test bz2 compression

import bz2

with bz2.open("bz2_compressed", "wb") as f:
    f.write(data)
# Test bz2 decompression

with bz2.open("bz2_compressed", "rb") as f:
    data = f.read()
    
    with bz2.open("bz2_decompressed", "wb") as g:
        g.write(data)
 
# Test zlib compression

import zlib

with open("zlib_compressed", "wb") as f:
    f.write(zlib.compress(data))
# Test zlib decompression

with open("zlib_compressed", "rb") as f:
    data = f
