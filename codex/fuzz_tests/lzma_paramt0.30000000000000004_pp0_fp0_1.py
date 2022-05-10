from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# b'Hello World!\n'

# lzma.LZMADecompressor.decompress() can be used as a context manager
# to automatically decompress data read from a file:

with open('hello.xz', 'rb') as input, \
     open('hello.txt', 'wb') as output:
     decompressor = LZMADecompressor()
     for block in iter(lambda: input.read(1024 * 1024), b''):
         output.write(decompressor.decompress(block))
     output.write(decompressor.flush())

# The flush() method is used to flush any remaining data from the
# decompressor object.

# The LZMADecompressor class also supports incremental decompression.
# To decompress a chunk of data, use the decompress() method.
# If the chunk of data was compressed using multiple LZMA blocks,
# the decompress() method will return empty bytes until the last
# block has been processed.

decompressor = LZMAD
