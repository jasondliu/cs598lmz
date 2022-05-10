import bz2
# Test BZ2Decompressor on an empty stream
try:
    bz2.BZ2Decompressor().decompress(b"")
except EOFError:
    pass
else:
    print("expected EOFError not raised")

# Test BZ2Decompressor.decompress() on a stream with no end-of-stream marker
try:
    bz2.BZ2Decompressor().decompress(b"xy")
except EOFError:
    pass
else:
    print("expected EOFError not raised")

# Test BZ2Decompressor.decompress() on a stream with invalid data after the
# end-of-stream marker
try:
    bz2.BZ2Decompressor().decompress(b"BZh91AY&SYxxy")
except IOError:
    pass
else:
    print("expected IOError not raised")

# Test BZ2Decompressor.decompress() on a stream with an truncated stream
try:
    bz2.BZ2Decompressor().decompress(b"BZh91
