from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMADecompressor.decompress(data, max_length=-1, format=FORMAT_AUTO, check=-1, memlimit=None, filters=None)
# Return a bytes object containing the decompressed version of the data.
# If the input data is not valid, a LZMAError exception is raised.
# If the data stream is corrupted, a LZMAError exception is raised.
# If the data stream is truncated, a LZMAError exception is raised.
# If the data stream is not truncated, but the decompressed data is longer than max_length bytes, a LZMAError exception is raised.
# If the data stream is truncated, the returned data may be shorter than max_length bytes.

# If the data stream is truncated, the returned data may be shorter than max_length bytes.
# If the data stream is not truncated, but the decompressed data is longer than max_length bytes, a LZMAError exception is raised.
# If the data stream is truncated, a LZMAError exception is raised.
