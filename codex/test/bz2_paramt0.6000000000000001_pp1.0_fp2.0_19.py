from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# Exercise 4
# Decompress the following compressed file using the zlib module.
# Use the zlib.decompress() function.
import zlib
