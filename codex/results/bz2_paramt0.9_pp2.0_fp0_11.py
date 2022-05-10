from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compress_string)

# Method 3
bz2_compress_string.decode("bz2")

# Method 4
print(zlib.decompress(zlib_compress_string))
