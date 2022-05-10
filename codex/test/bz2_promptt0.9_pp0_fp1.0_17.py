import bz2
# Test BZ2Decompressor.__init__()

decomp = bz2.BZ2Decompressor()
try:
    decomp.__init__()
except TypeError:
    print('TypeError')
