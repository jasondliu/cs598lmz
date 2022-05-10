from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMA library has a lot of options to fine-tune the compression process.
# For example, the format used by the XZ utility allows embedding multiple
# compressed streams into a single file, each one with its own header and
# footer. The LZMADecompressor class does not support this format, but the
# backports.lzma module provides a LZMAFile class that does.

# The LZMAFile class is a drop-in replacement for the built-in open() function,
# but it only supports opening files in binary mode.

