import lzma
# Test LZMADecompressor
import io
with open('sample.lzma', mode='rb') as f:
    file_content = f.read()

# Create a decompressor object
decompressor = lzma.LZMADecompressor()
# Feed in the compressed data chunk by chunk,
# and decompressed data will be available as
# `data` via the `decompress()` method.
decompressed_data = decompressor.decompress(file_content)

print(decompressed_data)

decompressed_data = decompressor.decompress(file_content)

# Verify that decompression worked
print(decompressed_data)

with open('sample.lzma', mode='rb') as f:
    with lzma.LZMAFile(f) as lzf:
        file_content = lzf.read()
        print(file_content)


import lzma
import random
print(random.random())
def test_lzma_speed(compresslevel=9):
    # Generating some sample data to compress
   
