from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello world!\n'

# Compress data
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'hello world!\n')
compressor.flush()

# Output: b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00'

# Compress data with preset
from lzma import LZMACompressor
