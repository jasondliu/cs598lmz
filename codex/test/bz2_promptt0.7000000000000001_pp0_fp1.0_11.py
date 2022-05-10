import bz2
# Test BZ2Decompressor
data = b'my compressed data goes here'

f = open('compressed_file.bz2', 'wb')
f.write(data)
f.close()

f = open('compressed_file.bz2', 'rb')

decompressor = bz2.BZ2Decompressor()
