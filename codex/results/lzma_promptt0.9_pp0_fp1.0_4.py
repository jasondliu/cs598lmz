import lzma
# Test LZMADecompressor objects for corruption after feeding data to them.
# The brotli library is able to generate a stream of decompressed data which
# passes the checksum, but which is internally corrupted. This simulates
# that situation, and verifies that the LZMADecompressor doesn't pass it
# through.

# Taken from https://github.com/python-brotli/python-brotli/issues/75#issuecomment-251939175

DECOMPRESSOR = lzma.LZMADecompressor()
# This chunk is invalid, but passes the crc32 check in the .xz format
INVALID_DATA = b'\x00\x02\xa1\x7fS\xdb8W\xe4A$\x9c[\xe4\xe63\xb1\xf4\x7f\x11\xac\x0b\x9c9\xc4\xed\t\xa4I\xb7\xb1\x8b\x94\xa9\x9dy\x15\xa8\xbc\xf3\x
