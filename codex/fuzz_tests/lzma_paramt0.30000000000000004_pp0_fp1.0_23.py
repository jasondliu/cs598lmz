from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# Output: b'Hello World!\n'

# The LZMA file format is described in the lzma module documentation.
# The LZMA decompressor supports the .xz format, the legacy .lzma format, and raw streams.
# The .xz format is a single-file compression format and does not provide archiving capabilities.
# The .lzma format is a legacy container format.
# Raw streams are useful for compressing data that is not a bytestring, such as objects serialized with pickle.
# The LZMA decompressor supports the FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, and FORMAT_RAW formats.
# The FORMAT_AUTO format is the default and detects the file format automatically.
# The FORMAT_XZ format is
