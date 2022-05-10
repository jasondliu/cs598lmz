import lzma
# Test LZMADecompressor with some garbage data.
# This should raise an EOFError exception.
lz = lzma.LZMADecompressor()
try:
    lz.decompress(b'\x00')
except EOFError:
    print('EOFError')
# Test LZMADecompressor with some garbage data.
# This should raise a ValueError exception.
lz = lzma.LZMADecompressor()
try:
    lz.decompress(b'\x00' * 100)
except ValueError:
    print('ValueError')
# Test LZMADecompressor with some garbage data.
# This should raise a TypeError exception.
lz = lzma.LZMADecompressor()
try:
    lz.decompress(b'\x00' * 100)
except TypeError:
    print('TypeError')
# Test LZMADecompressor with some garbage data.
# This should raise a BufferError exception.
lz = lzma.LZMADecompressor()
