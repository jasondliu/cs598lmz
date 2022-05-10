from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# Create a BZ2Compressor object
compressor = BZ2Compressor()

# Send data through the compressor and decompressor
for data in [b'a' * 100, b'b' * 100]:
    compressed = compressor.compress(data)
    print(compressed)
    print(BZ2Decompressor().decompress(compressed))

# Finish the compression process
remaining = compressor.flush()
print(remaining)
print(BZ2Decompressor().decompress(remaining))

# Compress a file in chunks
import bz2
import os

input_file = 'sample.txt'
output_file = input_file + '.bz2'

# Create a BZ2Compressor object
compressor = bz2.BZ2Compressor()

# Write one chunk at a time
with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
    for data in iter(lambda:
