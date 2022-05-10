import lzma
# Test LZMADecompressor
#
# This example demonstrates how to use LZMADecompressor to decompress
# data in a streaming fashion.

import lzma
import sys

# Read the compressed data from stdin
compressed_data = sys.stdin.buffer.read()

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
uncompressed_data = decompressor.decompress(compressed_data)

# Write the uncompressed data to stdout
sys.stdout.buffer.write(uncompressed_data)

# Finish the decompression process
decompressor.flush()

# Test LZMACompressor
#
# This example demonstrates how to use LZMACompressor to compress
# data in a streaming fashion.

import lzma
import sys

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read the uncompressed data from stdin
uncompressed_data = sys.stdin.buffer.read()

# Compress the data
comp
