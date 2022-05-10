import lzma
# Test LZMADecompressor()
comp = lzma.LZMADecompressor()
comp.decompress(b'BZh91AY&SY!')

# Test LZMACompressor()
comp = lzma.LZMACompressor()
comp.compress(b'foo')
comp.flush()


# Test the streaming interface

import io
# Test the streaming interface
with open('lorem.txt', 'rb') as lorem_in, \
        lzma.open('lorem.xz', 'wb') as lorem_out:
    lorem_out.write(lorem_in.read())

with lzma.open('lorem.xz', 'rb') as lorem_xz, \
        io.BufferedReader(lorem_xz) as lorem_in:
    # BufferedReader() must return the whole file once it has been read
    print(lorem_in.read())
    print(lorem_in.read())

# Test frombuffer() and tobuffer()

import os
# Test frombuffer() and tobuffer
