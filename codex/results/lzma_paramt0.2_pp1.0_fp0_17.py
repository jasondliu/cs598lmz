from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# decompress() method can be used to decompress a chunk of data at a time.
# This is useful when decompressing data incrementally.

# decompress() returns the data that was decompressed.
# If the end of the compressed data has been reached, an empty bytes object is returned.
# If the end of the compressed data has not been reached, the return value will be a bytes object
# containing the data that was decompressed.

# If the data stream is corrupted, a LZMAError exception will be raised.

# If the data stream is not a valid LZMA stream, a ValueError exception will be raised.

# If the data stream is valid but incomplete, a EOFError exception will be raised.

# If the data stream is valid but incomplete, a EOFError exception will be raised.

