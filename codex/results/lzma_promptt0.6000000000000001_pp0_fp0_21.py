import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()
# Decompress data
decomp = lz.decompress(data)
# Print decompressed data
print(decomp)

# Import LZMADecompressor class
from lzma import LZMADecompressor

# Create decompressor object
lz = LZMADecompressor()

# Decompress data
decomp = lz.decompress(data)

# Print decompressed data
print(decomp)

# Add a chunk of data to decompressor object
lz.decompress(data)

# Finish decompression
decomp2 = lz.flush()

# Print decompressed data
print(decomp2)

# Initialize a compressor object
lz = LZMACompressor(format=lzma.FORMAT_ALONE)

# Compress data
comp = lz.compress(b"Hello, World!")

# Print compressed data
print(comp)

# Finish compression
comp2 = lz.flush()

#
