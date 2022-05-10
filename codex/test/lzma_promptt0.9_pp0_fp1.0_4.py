import lzma
# Test LZMADecompressor objects for corruption after feeding data to them.
# The brotli library is able to generate a stream of decompressed data which
# passes the checksum, but which is internally corrupted. This simulates
# that situation, and verifies that the LZMADecompressor doesn't pass it
# through.

# Taken from https://github.com/python-brotli/python-brotli/issues/75#issuecomment-251939175

DECOMPRESSOR = lzma.LZMADecompressor()
# This chunk is invalid, but passes the crc32 check in the .xz format
