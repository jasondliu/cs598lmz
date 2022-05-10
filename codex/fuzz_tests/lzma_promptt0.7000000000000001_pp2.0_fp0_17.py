import lzma
# Test LZMADecompressor
lzd = lzma.LZMADecompressor()
lzd.decompress(b'\x5d\x00\x00\xff\xff')

import lzma
# Test LZMAEncoder
lze = lzma.LZMAEncoder()
lze.compress(b'hello')
lze.compress(b'world')
lze.flush()

import lzma
# Test LZMAEncoder
lzd = lzma.LZMADecompressor()
lzd.decompress(b'\x00\x04\x00\xff\xff\x00\x00\x00\x00')

import lzma
# Test LZMAEncoder
lze = lzma.LZMAEncoder()
lze.compress(b'hello')
lze.compress(b'world')
lze.flush()

import lzmaffi
# test lzmaffi.LZMADecompressor
lzd = lzmaff
