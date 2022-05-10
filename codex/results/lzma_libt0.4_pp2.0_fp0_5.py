import lzma
lzma.decompress(lzma.compress(b'hello world'))

# lzma.LZMADecompressor.decompress(data, max_length=-1)
# decompress(data, max_length=-1)
# Decompress *data*, returning uncompressed data as bytes.
# If *max_length* is nonnegative, returns at most *max_length* bytes of decompressed data.
# If this limit is reached and further output can be produced, *inflate* will raise an exception.
# No other data will be produced.
# In this case, any data found after the compressed data is ignored and saved in the unused_data attribute.
#
# If *max_length* is negative, or if there is no limit to the output, *decompress* will return all of the
# uncompressed data.
#
# Some formats, including ZIP and gzip, use an extra field in the file header
# to signal the use of different data compression methods.
# The *decompress* method recognizes these headers and adjusts accordingly.
# For example, the header for a ZIP
