import bz2
# Test BZ2Decompressor with various blocksizes.

# The first block is 1M of zeros, compressed to around 7k.
# The second block is filled with the alphabet, compressed to around 6k.
# The third block is filled with randomly chosen bytes, compressed around
# 19k.

# Each block is compressed in several ways. In the normal case,
# BZ2Compressor.compress() is called until the block is flushed.
# Some blocks are tested for compression with a flush at the end
# of each line (using newline as the separator) or after 1024 bytes
# (using _BZ2_MAX_UNUSED as the separator).

# The blocksize of the decompressor is varied from 0 to 30.
# For each blocksize, the compressed data is read in a variety of ways:
# bytewise, buffered with xreadlines, and readline.

# With a blocksize of 0, there should be no decompression at all.
# With a blocksize of 1, there should be decompression of the first block,
# but not the second, since it does not end in a newline.
#
