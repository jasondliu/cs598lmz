import bz2
# Test BZ2Decompressor class

data = open('lorem.txt', 'r').read() * 10

compressor = bz2.BZ2Compressor()

# Feed data in chunks
