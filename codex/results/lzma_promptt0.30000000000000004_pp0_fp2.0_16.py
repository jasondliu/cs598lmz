import lzma
# Test LZMADecompressor

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data
with open('data/sample.xz', 'rb') as input, open('data/sample.out', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
# Test LZMACompressor

# Create a LZMACompressor object
compressor = lzma.LZMACompressor()

# Compress data
with open('data/sample.txt', 'rb') as input, open('data/sample.xz', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))
    output.write(compressor.flush())
 
 
# Test LZMAFile

# Open a LZMA-compressed file in binary mode for
