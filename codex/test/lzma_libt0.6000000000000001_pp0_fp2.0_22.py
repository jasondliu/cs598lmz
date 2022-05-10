import lzma
lzma.LZMADecompressor().decompress(open('test.xz', 'rb').read())
