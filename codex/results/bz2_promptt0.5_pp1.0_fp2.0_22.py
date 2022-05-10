import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Try to decompress truncated data
try:
    decompressor.decompress(compressed_data[:-3])
except EOFError as err:
    print('ERROR:', err)

# Reset the decompressor
decompressor.decompress(compressed_data[-3:])

# Decompress the rest of the compressed data
decompressor.decompress(b'\x00\x00\x00\x00')

# Decompress the rest of the compressed data
decompressor.flush()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)

# Flush the compressor
compressor.flush()

# Create a BZ2File object
with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
       
