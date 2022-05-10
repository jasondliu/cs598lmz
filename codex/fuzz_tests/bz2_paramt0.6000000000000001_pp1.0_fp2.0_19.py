from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# Exercise 4
# Decompress the following compressed file using the zlib module.
# Use the zlib.decompress() function.
import zlib
zlib.decompress(b'\x78\x9c\xcb\x48\xcd\xc9\xc9\x57\x28\xcf\x2f\xca\x49\x01\x00\x0a\x38\xcb\x4b\xcd\x51\xc9\x49\x2d\x28\x28\x4a')

# Exercise 5
# Decompress the following compressed file using the lzma module.
# Use the lzma.decompress() function.
import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd
