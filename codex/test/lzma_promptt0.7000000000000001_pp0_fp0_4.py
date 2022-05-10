import lzma
# Test LZMADecompressor with a stream that contains a modified header to
# make sure that the header is properly checked and an exception is raised
# if it's invalid.

s = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00'

dec = lzma.LZMADecompressor()

# The header is invalid, but it's still possible to decompress the stream
