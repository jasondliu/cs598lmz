import bz2
# Test BZ2Decompressor class with a LZWDecompressor

import lzw
import io

data = bz2.compress(b'hello, world!')
with bz2.BZ2Decompressor() as dec:
    with lzw.LZWDecompressor(dec) as lzw_dec:
        print(lzw_dec.decompress(data))

# Test BZ2Compressor class with a LZWCompressor

import lzw

data = b'hello world!hello world!hello world!hello world!'
with bz2.BZ2Compressor() as comp:
    with lzw.LZWCompressor(comp) as lzw_comp:
        print(lzw_comp.compress(data))
        print(lzw_comp.flush())
 
# Test BZ2Compressor and BZ2Decompressor classes with a LZWCompressor and LZWDecompressor, respectively,
# to compress, then decompress the data

import lzw
import io

data = b'
