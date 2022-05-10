import bz2
# Test BZ2Decompressor
data = b'my compressed data goes here'

f = open('compressed_file.bz2', 'wb')
f.write(data)
f.close()

f = open('compressed_file.bz2', 'rb')

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(f.read())

f.close()

print(result)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
result = bz2.compress(data)

print(result)

# Test BZ2File
#
# BZ2File is a context manager.
#
# Since the file is not actually read until the first read operation,
# this context manager will not raise any exceptions if the file does
# not exist.
#
# BZ2File is also an iterator, so this context manager supports multiple
# iterations.
#
# The compression level is 1 by default, and can be changed by passing
# the compresslevel parameter.
#
# The maximum compression level
