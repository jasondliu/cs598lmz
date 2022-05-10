from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/home/zack/Downloads/enwik8.lzma', 'rb').read()[0:100000])

import lzma
lzc = lzma.LZMACompressor()
lzc.compress(b'Hello, world!')

lzc.flush()

lzd = lzma.LZMADecompressor()
lzd.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x00')

import zlib
zlib.compress(b'Hello, world!')

zlib.decompress(b'x\x9c+\xca\xc9\xc8,V\x00\x0b\x05\xd0\x80\x00\
