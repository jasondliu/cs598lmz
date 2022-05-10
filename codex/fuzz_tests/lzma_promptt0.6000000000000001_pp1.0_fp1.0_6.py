import lzma
# Test LZMADecompressor with a file containing a corrupted LZMA stream
# (missing the last byte).

with lzma.open(TESTFN, "rb") as f:
    c = lzma.LZMADecompressor()
    f.seek(-1, 2)
    f.truncate()
    # Read a few bytes to make sure nothing explodes.
    f.read(10)
    f.close()

with open(TESTFN, "rb") as f:
    c = lzma.LZMADecompressor()
    f.seek(-1, 2)
    f.truncate()
    # Read a few bytes to make sure nothing explodes.
    f.read(10)
    f.close()
