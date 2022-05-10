from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfe\x4c\x5a\x4f\xff\x00\x00\x04\x00\x01\x0d')
# b'hello world\n'
</code>

