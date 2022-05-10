from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMA format supports a wide range of compression options,
# including the ability to set the compression level, the number of
# dictionary bits, and the number of literal context bits.
#
# The LZMAFile class supports all of these options, and also
# provides a simple interface for reading and writing files.
#
# For example, to compress a file using the default options:

from lzma import LZMAFile
with open('lorem.txt', 'rb') as input, \
     LZMAFile('lorem.txt.xz', 'w') as output:
    output.writelines(input)

# To decompress the file again:

with LZMAFile('lorem.txt.xz', 'r') as input, \
