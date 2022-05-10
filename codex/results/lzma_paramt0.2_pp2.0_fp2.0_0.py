from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello world!\n'

# The LZMA format supports a wide range of compression settings,
# and the lzma module supports all of them.
# The format is also capable of representing uncompressed data,
# although the lzma module does not support that.

# The LZMA format is also used in the .xz file format,
# which is a single-file container format.
# The lzma module does not support .xz files.
# To read and write .xz files, use the XZFile class in the backports.lzma module.

# The LZMA format is also used in the .7z file format,
# which is a multi-file container format.
# The lzma module does not support .7z files.
# To
