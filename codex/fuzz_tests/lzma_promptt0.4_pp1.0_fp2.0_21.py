import lzma
# Test LZMADecompressor

# Decompress the test data
with lzma.open('lzma_compressed.xz', 'rb') as input, open('lzma_decompressed.txt', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
    output.write(decompressor.flush())

# Verify the decompressed data
with open('lzma_decompressed.txt', 'rb') as f:
    data = f.read()
print(data)

# Output the decompressed data to the screen
with open('lzma_decompressed.txt', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        print(decompressor.decompress(chunk))
    print(decompressor
