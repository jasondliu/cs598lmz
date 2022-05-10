from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xb6\x00\x00K\x01\x00\x00\x00K')
LZMADecompressor().flush()
