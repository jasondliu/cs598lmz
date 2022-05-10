import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Read one compressed block
compressed_block = file.read(1024)

# Decompress the compressed block
decompressed_block = decompressor.decompress(compressed_block)

# Print the first 100 bytes of the decompressed block
print(decompressed_block[:100])
# Create a BZ2File object
file = bz2.BZ2File('data/armenian-online-journals.csv.bz2')

# Print the info attribute
print(file.info)

# Create a BZ2File object
file = bz2.BZ2File('data/armenian-online-journals.csv.bz2')

# Read the first 3 lines
print(file.readline())
print(file.readline())
print(file.readline())
# Import pandas
import pandas as pd

# Create a BZ2File object
file = bz2.BZ2File('data/armenian-online-journals.
