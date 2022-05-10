import lzma
# Test LZMADecompressor.flush()

# The flush() method is used to get more data from the decompressor.
# It returns an empty bytes object when no more data can be obtained.
# Even when the flush() method returns an empty bytes object,
# the LZMADecompressor object may still have some data to be read.

# This test tries to decompress a file with multiple concatenated
# LZMA compressed streams.

# The test uses a file with the following structure:
#  - a "magic" number (used for testing)
#  - the number of compressed streams
#  - a compressed stream
#  - a compressed stream
#  - ... (repeated for the number of streams specified)
#  - a compressed stream
#  - a "magic" number

# The test then decompresses the file, and checks that:
#  - the two magic numbers match
#  - the decompressed data is correct

# The compressed data for each stream consists of:
#  - a "magic" number
#  - the length of the uncompressed data
#  - the uncompressed data
#  - a "
