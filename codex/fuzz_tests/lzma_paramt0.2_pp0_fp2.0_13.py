from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# decompress(data, max_length=-1)
# max_length is the maximum allowed length of the decompressed data.
# If the decompressed data would be longer than max_length,
# raise an EOFError.
# If max_length is negative or omitted,
# or if there is no limit to the length of the decompressed data,
# decompress() will return as much of the decompressed data as possible.
# In this case, the return value may be longer than data.

# decompress(data, max_length=0)
# If max_length is zero, decompress() will return an empty bytes object.

# decompress(data, max_length=1)
# If max_length is one, decompress() will return a bytes object containing the first byte of the decompressed data
