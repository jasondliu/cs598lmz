from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x0c\xff\xff\xff\xff\xff\xff\xff\x04\x00\x23\x00')
# b'hello world!'
</code>

