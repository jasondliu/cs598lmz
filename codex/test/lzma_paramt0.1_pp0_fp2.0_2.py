from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello world!\n'

# The LZMA library supports a number of different compression modes.
# The default mode is MODE_XZ, which is the mode used by the .xz file format.
# The other modes are MODE_ALONE, MODE_RAW, and MODE_FAST.
# The MODE_ALONE mode is used by the .lzma file format.
# The MODE_RAW mode is used by the .lzma file format, but only for files with a .lzma file extension.
# The MODE_FAST mode is used by the .lzma file format, but only for files with a .lzma file extension.
# The MODE_FAST mode is used by the .lzma file format, but only for files with
