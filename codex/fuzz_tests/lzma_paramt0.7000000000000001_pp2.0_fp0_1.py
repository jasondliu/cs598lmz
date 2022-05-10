from lzma import LZMADecompressor
LZMADecompressor().decompress(b'X\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x04J\xd6\x04\x00')
# b'hello'

decompressor = LZMADecompressor()
compressed = b'X\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x04J\xd6\x04\x00'
decompressor.decompress(compressed)
# b'hello'

decompressor.decompress(b'hello')
# b''

decompressor.flush()
# b'hello'

# Writing compressed data to a file
import lzma

with lzma.open('file.xz', 'wt') as f:
    f.write('Hello, world!')


# Reading compressed data from a file
import lzma

with lzma.open('file.xz', 'rt') as f:
