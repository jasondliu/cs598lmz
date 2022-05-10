from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('test.bz2', 'rb').read())
