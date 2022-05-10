import lzma
# Test LZMADecompressor with a file containing a few blocks of various kinds.

# This file was generated using the following command:
# lzma --format=lzma --lzma1=preset=9,dict=32KiB \
#  --match-finder=hc4 --extreme --fb=273 --block-size=8KiB \
#  -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 --keep -o lzma_file.xz /dev/zero

# The file consists of the following blocks:
# - 0xFF bytes
# - 0x00 bytes
# - 0xFF bytes (boundary between two blocks)
# - 0x00 bytes
# - 0xFF bytes (boundary between two blocks)
# - 0x00 bytes
# - 0xFF bytes (boundary between two blocks)
# - 0x00 bytes
# - 0xFF bytes (boundary between two blocks)

# Each of the first four blocks is followed by an empty block.
# This means that the blocks are not actually empty, but instead
#
