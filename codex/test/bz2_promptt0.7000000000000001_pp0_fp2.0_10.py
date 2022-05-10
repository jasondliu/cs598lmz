import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()
decompressor = bz2.BZ2Decompressor()
