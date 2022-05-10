import bz2
# Test BZ2Decompressor: compression and decompression
# Round-trip data through BZ2Compressor and BZ2Decompressor
# BZ2Compressor: where to feed in data, and how to get compressed data out
# BZ2Decompressor: where to feed in compressed data, and how to get uncompressed data out

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# Feed in data to be compressed
a_string = "A somewhat long string of ASCII text, just for fun."
compressed_a_string = compressor.compress(a_string)

# Feed in the compressed data to be decompressed
decompressed_a_string = decompressor.decompress(compressed_a_string)

print(decompressed_a_string)

# NOTE:
#	compressor.compress()			==>	Returns the remaining data left in the internal buffer
#	decompressor.decompress()		==>	Returns the remaining data left in the internal buffer

# Output:
#	A somewhat long
