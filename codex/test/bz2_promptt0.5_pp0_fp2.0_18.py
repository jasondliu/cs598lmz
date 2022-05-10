import bz2
# Test BZ2Decompressor.__init__

try:
    bz2.BZ2Decompressor()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.__init__ with invalid args
try:
    bz2.BZ2Decompressor(10)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.decompress() with invalid args
try:
    bz2.BZ2Decompressor().decompress(10)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.flush() with invalid args
try:
    bz2.BZ2Decompressor().flush(10)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.decompress()
d = bz2.BZ2Decompressor()
