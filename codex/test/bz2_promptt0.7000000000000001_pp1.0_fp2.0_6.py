import bz2
# Test BZ2Decompressor and BZ2Compressor

data = b"1234567890" * 100000
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# Feeding bytes to the compressor returns blocks of compressed data,
# which may be empty until it has enough data for a full compressed
# block.
