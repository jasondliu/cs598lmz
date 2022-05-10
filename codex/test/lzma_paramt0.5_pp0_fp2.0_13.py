from lzma import LZMADecompressor
LZMADecompressor().decompress(open('compressed.lzma', 'rb').read())

# b'Hello World!'
