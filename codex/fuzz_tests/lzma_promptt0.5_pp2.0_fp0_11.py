import lzma
# Test LZMADecompressor

# The first two bytes of an LZMA stream are the dictionary size
# encoded as a little-endian unsigned integer.

# Dictionary size is 2^n where n is in the range [0, 40]

# The dictionary size is the largest number of bytes that LZMA can
# use to look for matches.

# The larger the dictionary size, the better the compression ratio
# but the slower the compression and decompression.

# If the dictionary size is too small, then the compression ratio
# will be poor.

# If the dictionary size is too large, then the compression and
# decompression will be slow.

# LZMA uses a default dictionary size of 2^24.

# LZMA decompression is fast and requires little memory, regardless
# of the dictionary size.

# The LZMADecompressor class supports incremental decompression.

# The decompress() method can be called multiple times, as long as
# the data to be decompressed is concatenated and passed as one
# parameter to decompress().

# The uncompressed data is returned as a bytes object.

#
