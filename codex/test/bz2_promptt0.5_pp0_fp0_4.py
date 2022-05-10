import bz2
# Test BZ2Decompressor.__init__()

decomp = bz2.BZ2Decompressor()

try:
    decomp.decompress(b"")
except IOError as e:
    print(e)
# Test BZ2Decompressor.__init__() with a small buffer

