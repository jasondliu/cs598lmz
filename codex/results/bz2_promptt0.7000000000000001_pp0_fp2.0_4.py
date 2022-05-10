import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
# Decompress a single block of data

decompressed_data = decompressor.decompress(single_block_compressed_data)
decompressed_data

# b"This is the entire message."
# Decompress multiple blocks of data

decompressor.decompress(multiple_block_compressed_data)

# b"This is the entire message."
# It's possible to call decompress() multiple times to decompress the data in stages.
# This is useful when the compressed data is too large to fit in memory all at once.

decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(
    multiple_block_compressed_data[:100])
decompressed_data

# b"This is t"

decompressed_data = decompressor.decompress(
    multiple_block_compressed_data[100:])
decompressed_data

# b"he entire message."

# bz2
