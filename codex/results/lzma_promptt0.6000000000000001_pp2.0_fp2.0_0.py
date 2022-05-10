import lzma
# Test LZMADecompressor
assert LZMADecompressor().decompress(
    lzma.compress(b'abcdefghijklmnopqrstuvwxyz')) == b'abcdefghijklmnopqrstuvwxyz'
# Test LZMADecompressor.decompress() with max_length
lzc = LZMADecompressor()
lzc.decompress(lzma.compress(b'abcdefghijklmnopqrstuvwxyz'), max_length=5)
# Test LZMADecompressor.decompress() with max_length
lzc.decompress(lzma.compress(b'abcdefghijklmnopqrstuvwxyz'), max_length=25)
# Test LZMADecompressor.decompress() with max_length
lzc.decompress(lzma.compress(b'abcdefghijklmnopqrstuvwxyz'))
# Test LZMADecompressor.decompress()
