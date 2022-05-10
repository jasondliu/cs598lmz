from lzma import LZMADecompressor
LZMADecompressor().decompress(open('test.xz', 'rb').read())
