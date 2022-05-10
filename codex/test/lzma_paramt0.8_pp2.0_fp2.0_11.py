from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x01')
# b'\x02'
