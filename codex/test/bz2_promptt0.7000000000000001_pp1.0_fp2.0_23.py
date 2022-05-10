import bz2
# Test BZ2Decompressor and compressobj

for compressor in (bz2.BZ2Compressor, bz2.BZ2Decompressor):
    obj = compressor()
