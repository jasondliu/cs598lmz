import bz2
# Test BZ2Decompressor's readline() implementation against the same data 
# decompressed using bz2.decompress() and bz2.BZ2Decompressor.

NUM_LINES = 10000

data = bz2.decompress(bz2.compress(b'data '*NUM_LINES))

