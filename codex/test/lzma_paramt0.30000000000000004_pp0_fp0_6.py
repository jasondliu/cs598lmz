from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# uncompressed data is b'\x00' * 1000000

# decompress a stream of data
from lzma import LZMADecompressor
decompressor = LZMADecompressor()
with open('lzma_compressed.xz', 'rb') as input, \
     open('uncompressed.bin', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
