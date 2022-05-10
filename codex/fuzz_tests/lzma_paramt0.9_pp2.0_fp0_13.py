from lzma import LZMADecompressor
LZMADecompressor()
del LZMADecompressor

try:
    from lzma import LZMADecompressor
except ImportError:
    pass
else:
    raise AssertionError

import lzma
dec = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
del lzma, dec

import lzma
dec = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
dec.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00')
del lzma, dec

dec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
try:
    dec.decompress(b'\xfd
