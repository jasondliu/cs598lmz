from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMADecompressor class also supports the context management protocol.
# This allows you to use it in a with statement, which will automatically close the decompressor when the with statement is exited.

from lzma import LZMADecompressor
with LZMADecompressor() as decompressor:
    decompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMADecompressor class also supports the context management protocol.
# This allows you
