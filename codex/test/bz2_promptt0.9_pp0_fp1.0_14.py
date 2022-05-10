import bz2
# Test BZ2Decompressor on empty data.
bz2.decompress(b'') is b''

# Test compress_output with small input.
