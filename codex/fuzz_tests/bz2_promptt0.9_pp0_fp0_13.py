import bz2
# Test BZ2Decompressor
data = open('compressed.bz2', 'rb').read()
print(len(data))

# decompress()
decompressor = bz2.BZ2Decompressor()
plain = decompressor.decompress(data)
print(len(plain))
print(plain[:20])

# decompress()
plain = bz2.decompress(data)
print(len(plain))
print(plain[:20])

# incremental stuff
# -> if we get a partial stream of data, we can continue decompressing it
#    provided that we keep that BZ2Decompressor instance around
decompressor = bz2.BZ2Decompressor()
input = open('compressed.bz2', 'rb')
# we read the first 30 bytes of the file
chunk, size, COMPRESS_START_SIZE, COMPRESS_STOP_SIZE = input.read(30), 0, bz2.__version__.startswith('0.9'), 1
# chunk -> bytes
print(len(chunk))

# we know from reading the
