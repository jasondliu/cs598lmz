from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output:
# b'The quick brown fox jumps over the lazy dog'
</code>
LZMA files can be concatenated, so it is possible that only part of the file is LZMA compressed.

