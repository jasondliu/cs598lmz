import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('lorem.txt.xz', 'rb') as input, open('lorem_decompressed.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        result = decompressor.decompress(chunk)
        if result:
            output.write(result)

# Flush any remaining data
result = decompressor.flush()
output.write(result)

# Check that the output file is the same as the original
with open('lorem.txt', 'rb') as f:
    original = f.read()
with open('lorem_decompressed.txt', 'rb') as f:
    result = f.read()
assert original == result
 
# Test LZMADecompressor with multiple chunks

# Create a decompressor object
decompressor = lzma.LZMADecompressor()


