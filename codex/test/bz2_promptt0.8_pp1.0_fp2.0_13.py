import bz2
# Test BZ2Decompressor
data = open(bz2.__file__, 'rb').read(100)
print(data)
print('length:', len(data))
