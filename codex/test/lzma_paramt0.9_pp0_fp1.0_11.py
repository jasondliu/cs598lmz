from lzma import LZMADecompressor
LZMADecompressor().decompress(open('foo.xz', 'rb').read())
