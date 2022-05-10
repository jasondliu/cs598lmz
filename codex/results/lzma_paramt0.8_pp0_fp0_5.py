from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x{fd}7\x{fd}\xff\x{fd}7\x{fd}\xfe')
with open(filename, 'rb') as f:
    decompressor = LZMADecompressor()
    data = decompressor.decompress(f.read())
data

import lzma
with lzma.open(filename) as f:
    contents = f.read()
contents
