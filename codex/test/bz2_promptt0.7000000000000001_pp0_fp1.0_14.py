import bz2
# Test BZ2Decompressor on an empty stream
try:
    bz2.BZ2Decompressor().decompress(b"")
except EOFError:
    pass
else:
    print("expected EOFError not raised")

# Test BZ2Decompressor.decompress() on a stream with no end-of-stream marker
