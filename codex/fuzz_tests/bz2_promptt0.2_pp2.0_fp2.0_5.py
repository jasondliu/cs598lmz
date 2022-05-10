import bz2
# Test BZ2Decompressor.__init__()

decomp = bz2.BZ2Decompressor()
try:
    decomp.__init__()
except TypeError:
    print('TypeError')
# Test BZ2Decompressor.decompress()

decomp = bz2.BZ2Decompressor()
try:
    decomp.decompress()
except TypeError:
    print('TypeError')
# Test BZ2Decompressor.decompress()

decomp = bz2.BZ2Decompressor()
try:
    decomp.decompress(b'', 0)
except TypeError:
    print('TypeError')
# Test BZ2Decompressor.decompress()

decomp = bz2.BZ2Decompressor()
try:
    decomp.decompress(b'', 0, 0)
except TypeError:
    print('TypeError')
# Test BZ2Decompressor.decompress()

decomp = bz2.BZ2Decompressor()
try:
    decomp.decompress(
