from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b"abc\n"

# The lzma module also supports LZMA2, which is a newer file format.
# LZMA2 files have a little more overhead than LZMA files, but they can be
# decompressed faster and are more flexible.
# LZMA2 files can be decompressed using the same LZMADecompressor class,
# but you need to pass the format parameter to the decompressor constructor.
# For example:

from lzma import LZMADecompressor
decompressor = LZMADecompressor(format=lzma.FORMAT_XZ)
decompressor.decompress(data)

# b"abc\n"

# LZMA files are usually a little smaller than LZMA2 files, but they are
# also a little slower to compress.
# LZMA2 files are usually a little larger than LZMA files, but they are
# also a little faster to compress.
# The lzma module also supports the legacy lzma format, which is the format
#
