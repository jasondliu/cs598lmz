import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    input_bytes = f.read()

decompressor = lzma.LZMADecompressor()
output_bytes = decompressor.decompress(input_bytes)
output_bytes

with open('test.txt', 'wb') as f:
    f.write(output_bytes)
    
with open('test.txt', 'rb') as f:
    print(f.read())

# Test LZMACompressor

with open('test.txt', 'rb') as f:
    input_bytes = f.read()

compressor = lzma.LZMACompressor()
output_bytes = compressor.compress(input_bytes)
output_bytes += compressor.flush()

with open('test.xz', 'wb') as f:
    f.write(output_bytes)
    
with open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile

