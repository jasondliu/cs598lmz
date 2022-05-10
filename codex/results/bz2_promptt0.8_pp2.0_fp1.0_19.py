import bz2
# Test BZ2Decompressor.
decompressor = bz2.BZ2Decompressor()
data = open(sys.argv[2], 'rb').read(100)
# Test decompress()
print decompressor.decompress(data)
# Test flush()
print decompressor.flush()
