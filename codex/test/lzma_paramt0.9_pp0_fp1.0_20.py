from lzma import LZMADecompressor
LZMADecompressor().decompress(b"")
b'\x00\x00\x00\x01\xff\xff'
b'\0\0\0\1\xff\xff'
