from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# b'This is the text to be compressed. '

# The LZMADecompressor class also supports the context manager protocol.
# Like the BZ2Decompressor, this allows decompression with less
# boilerplate code.

with LZMADecompressor() as decompressor:
    decompressed = decompressor.decompress(compressed)

# b'This is the text to be compressed. '

# The LZMADecompressor supports a number of optional arguments which
# control the format of the input data:

# format
# Bytes indicating the format of the input data.
# The default value is FORMAT_AUTO.

# FILTER_LZMA1, FILTER_LZMA2
# Indicates that the input data consists of one or more LZMA1 or LZMA2
# streams.

# FILTER_DELTA
# Indicates that the input data consists of one or more Delta streams.

# FILTER_X86
# Indicates that the input data consists of one or more x86
