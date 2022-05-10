from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# Compress

from lzma import LZMACompressor
LZMACompressor().compress(b'hello')

# Output: b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'

# Compress with a preset

from lzma import LZMACompressor
LZMACompressor(preset=9 | LZMA_PRESET_EXTREME).compress(b'hello')

# Output: b'\xfd\x37\x7a\x58\x5a\x00\x00
