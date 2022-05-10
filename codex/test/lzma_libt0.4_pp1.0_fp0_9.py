import lzma
lzma.LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# output: b'hello'

# If you want to decompress data that was compressed using the LZMA1
# algorithm, you can use the LZMADecompressor.decompress() method:

import lzma
