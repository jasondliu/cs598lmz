import bz2
# Test BZ2Decompressor.__init__()

try:
    bz2.BZ2Decompressor()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.decompress()

