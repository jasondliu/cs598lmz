from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=None)
# Return the decompressed data as bytes.
# If the max_length parameter is specified, at most max_length bytes will be decompressed.
# If the decompressed length is not known in advance, and the data stream is not terminated by EOF,
# the decompressor will raise LZMAError if more than max_length bytes are read.

# lzma.LZMADecompressor.flush()
# Return the remaining decompressed data as bytes.
# This method should be called only after the entire input data has been decompressed.
# If the input data was not terminated by EOF, the decompressor may raise LZMAError.

# lzma.LZMADecompressor.eof
# A boolean indicating whether the end of the compressed data stream has been reached.
# This is only meaningful after decompressing the entire input data stream.
# If the input data was not terminated by EOF, the decompressor may raise LZMAError.

# l
