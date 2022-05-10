from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

# decompress lzma (xz)
from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x00\x10\x00\x00\x00')
