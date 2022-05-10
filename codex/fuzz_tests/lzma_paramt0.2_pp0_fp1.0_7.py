from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# Compress a file:

with open('lorem.txt', 'rb') as input, open('lorem.xz', 'wb') as output:
    compressor = LZMACompressor()
    output.write(compressor.compress(input.read()))
    output.write(compressor.flush())

# Decompress a file:

with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# The LZMAFile class implements a file-like interface
