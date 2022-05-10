import lzma
# Test LZMADecompressor
# http://www.python.org/dev/peps/pep-0274/

from lzma import LZMADecompressor
from struct import unpack

# fileobj = open('test.xz', 'rb')
#
# # Read the .xz magic bytes.
# fileobj.read(6)
#
# # Read and parse the Stream Header.
# (total_size,) = unpack('<Q', fileobj.read(8))
#
# dec = LZMADecompressor()
# data = fileobj.read(1024 * 1024)
# while data:
#     data = dec.decompress(data)
#     if data:
#         print(data)
#     data = fileobj.read(1024 * 1024)

# print(dec.unused_data)
# print(total_size)
# print(dec.eof)
# print(dec.unconsumed_tail)

# print(dec.decompress('\x00\x00\x00\x00\x00\x00\x
