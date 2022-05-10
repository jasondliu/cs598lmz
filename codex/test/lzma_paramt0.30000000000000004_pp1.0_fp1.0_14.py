from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/tmp/foo.xz', 'rb').read())
