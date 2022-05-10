import bz2
# Test BZ2Decompressor

bz2_data = open('../bz2data.bin', 'rb').read()

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Feed the entire compressed data to the decompressor
uncompressed_data = decompressor.decompress(bz2_data)

# Check if the decompression worked
print(uncompressed_data == "This is the original text before being compressed.")

# Feed the compressed data in small chunks to the decompressor
decompressor = bz2.BZ2Decompressor()

for chunk in range(0, len(bz2_data), 100):
    uncompressed_data += decompressor.decompress(bz2_data[chunk:chunk+100])

assert(uncompressed_data == "This is the original text before being compressed.")

# Test BZ2Compressor
# Create a BZ2Compressor object
compressor = bz2.BZ2Compressor()

# Give the compressor some data to compress
for i in range
