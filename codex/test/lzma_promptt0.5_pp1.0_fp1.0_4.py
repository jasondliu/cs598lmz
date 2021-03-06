import lzma
# Test LZMADecompressor. 

# The test data was generated by the xz utility, using the command:
# xz -9 -k -e --memlimit-compress=16MiB --memlimit-decompress=16MiB
#     --check=crc32 --format=raw

# The test data is a random data stream, compressed with xz. The size of
# each compressed block is random and varies between 1 and 64 KiB.

# The test data is a byte stream, where each byte is a random number.
# The length of the byte stream is about 1 GiB.

# For each compressed block, the decompressor must return the correct
# uncompressed data.

# After decompressing the whole test data, the decompressor must return
# the correct checksum.

# In addition to the test data, the test script also verifies that
# decompressing truncated compressed data works as expected.

