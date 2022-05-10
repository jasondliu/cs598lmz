import bz2
# Test BZ2Decompressor.decompress() method.
#
# Create a decompressor object, feed it compressed data,
# and get decompressed data.

# Compress a short text.
compressed_data = bz2.compress(b"Hello World")

# Create a decompressor object.
decompressor = bz2.BZ2Decompressor()

# Decompress the compressed data.
decompressed_data = decompressor.decompress(compressed_data)

# Check the data is correct.
print("Decompressed data:", decompressed_data)
print("Original data:", b"Hello World")

# Test BZ2Decompressor.decompress() method.
#
# Create a decompressor object, feed it compressed data,
# and get decompressed data.

# Compress a short text.
compressed_data = bz2.compress(b"Hello World")

# Create a decompressor object.
decompressor = bz2.BZ2Decompressor()

# Decompress the compressed data.
