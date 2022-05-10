from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
# b'Hello Python world!\n'

# Create a decompressor object, and decompress the compressed data
decompressor = LZMADecompressor()
print(decompressor.decompress(data1))
# b'foobar'
print(decompressor.unused_data)
# b''

print(decompressor.decompress(data2))
# b''
print(decompressor.unused_data)
# b'hello'

print(decompressor.unconsumed_tail)
# b''
# `decompressor.decompress()` returns any unconsumed data from the end of the
# compressed data blocks processed so far.

# `decompressor.unconsumed_tail` contains the unconsumed data from the last
# call to `decompressor.decompress()`.

# After decompression is complete, these two attributes will always contain
# the same data.
