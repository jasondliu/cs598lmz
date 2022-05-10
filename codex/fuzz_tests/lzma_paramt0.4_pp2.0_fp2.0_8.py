from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'The quick brown fox jumps over the lazy dog.'

# The LZMA compressor can also be used in a streaming fashion.
# For example, to read a compressed file one block at a time:

from lzma import LZMADecompressor

with open('example.xz', 'rb') as input, open('example.out', 'wb') as output:
    decompressor = LZMADecompressor()
    while True:
        block = input.read(1024)
        if not block:
            break
        output.write(decompressor.decompress(block))

# The LZMADecompressor.unused_data attribute contains any data that
# was supplied to the decompressor that could not be consumed.
# This can be used to pick up data where the last decompress() call left off.

# The LZMADecompressor.eof attribute is set to True when the end
# of the compressed data has been reached.
# This can be used to write the final bytes of the output file:

from
