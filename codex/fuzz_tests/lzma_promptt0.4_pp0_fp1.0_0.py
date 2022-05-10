import lzma
# Test LZMADecompressor.decompress()

# The test data is from the LZMA SDK.

# The first byte of the file is the dictionary size.
# The second byte of the file is the match finder.
# The rest of the file is the compressed data.

# The dictionary size is in the range [0, 8].
# The match finder is in the range [0, 2].

# The LZMA SDK uses the following dictionary sizes:
#   0:  2^18 bytes
#   1:  2^20 bytes
#   2:  2^21 bytes
#   3:  2^22 bytes
#   4:  2^23 bytes
#   5:  2^24 bytes
#   6:  2^26 bytes
#   7:  2^27 bytes
#   8:  2^29 bytes

# The LZMA SDK uses the following match finders:
#   0:  BT2
#   1:  BT4
#   2:  BT4B

# The LZMA SDK uses the following filters:
#   0:  BCJ
#
