from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("compressed.bz2", "rb").read())

# Using lz4 compression
