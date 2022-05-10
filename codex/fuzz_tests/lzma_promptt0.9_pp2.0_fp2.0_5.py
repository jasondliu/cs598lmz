import lzma
# Test LZMADecompressor as a context manager
path = bz2.compress(os.urandom(10))
with lzma.LZMADecompressor() as decompressor:
    data = decompressor.decompress(path)

# Test LZMADecompressor as an object
decompressor = lzma.LZMADecompressor()
decompressor.decompress(path)
decompressor.flush()

# Issue #9066: make sure that LZMADecompressor.decompress returns at most
# *unconsumed_tail* bytes of unconsumed data
decompressor = lzma.LZMADecompressor()
fragment = decompressor.decompress(path, 1)
fragment
len(fragment)
# Issue #2197: check that we can decompress a non-empty bytestring followed by
# an empty bytestring
decompressor = lzma.LZMADecompressor()
decompressor.decompress(path) + decompressor.decompress(b'')

# Test
