from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=-1)
# Decompress *data*, returning uncompressed data as bytes.
# If *max_length* is nonnegative, returns at most *max_length* bytes of
# decompressed data. If this limit is reached and further output can be
# produced, *decompress* will raise an *EOSError*.
#
# If zero bytes of input are given, returns zero bytes of output and only
# requires that *flush* be called on the compressor object.
#
# After *decompress* has returned, some of the input data may still be stored in
# internal buffers for later processing.
# Call the *flush* method to clear these buffers.
#
# If any data was found after the end of the compressed data,
# *decompress* will raise an *EOFError*.
#
# *decompress* can be used to decompress data incrementally.
#
# For one-shot decompression, use the decompress() convenience function.

# lz
