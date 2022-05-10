import lzma
# Test LZMADecompressor.decompress() on a large file.

# Uncompressed size of test file.
# Uncompressed size of test file.
TEST_SIZE = 100 * 1024 * 1024

# Compressed size of test file.
TEST_SIZE_COMPRESSED = 4 * 1024 * 1024

# Compressed data.
TEST_DATA = b'x' * TEST_SIZE_COMPRESSED

# Compressed data with a trailing garbage.
TEST_DATA_GARBAGE = TEST_DATA + b'y' * 1024

# Compressed data with a trailing garbage.
TEST_DATA_GARBAGE2 = TEST_DATA + b'y' * 100000

# Compressed data with a trailing garbage.
TEST_DATA_GARBAGE3 = TEST_DATA + b'y' * 1000000

# Compressed data with a trailing garbage.
TEST_DATA_GARBAGE4 = TEST_DATA + b'y' * 10000000


