import bz2
# Test BZ2Decompressor.flush()
decomp = bz2.BZ2Decompressor()
decomp.decompress(b'BZ')
try:
    decomp.flush()
except EOFError:
    pass
else:
    print("testing BZ2Decompressor.flush() didn't raise EOFError")
