from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/dev/zero', 'rb').read())

