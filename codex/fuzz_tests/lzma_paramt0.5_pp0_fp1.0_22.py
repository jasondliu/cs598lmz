from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# LZMA is a lossless compression, and it can compress and decompress
# faster than bz2.
# However, it does not have a stream-based compressor/decompressor
# interface like bz2 does.

# The lzma module also supports a command-line interface that can be
# used to compress and decompress files.
# This is useful for situations where you want to compress a file
# using the .xz format, which is not supported by the bz2 module.

# The lzma module can be used to compress and decompress data in
# the LZMA and XZ formats.
# It provides a stream-based compressor and decompressor classes
# for incremental processing.
# The decompressor class can be used to decompress data in the
# LZMA, XZ, and legacy LZMA formats.
# The compressor class only supports the XZ format.
# The module also provides a class for decompressing data incrementally
# using the LZMA format, but it does not support compressing data.
# The module also supports a command-line
