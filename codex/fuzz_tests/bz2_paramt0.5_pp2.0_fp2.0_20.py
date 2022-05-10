from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# Compress data

import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# Compress data using context manager

import bz2
original_data = b'This is the original text.'
with bz2.BZ2File('example.bz2', 'wb') as output:
    output.write(original_data)

with bz2.BZ2File('example.bz2', 'rb') as input:
    print(input.read())

# Compress data incrementally

import bz2
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'This is the original text.'))
print
