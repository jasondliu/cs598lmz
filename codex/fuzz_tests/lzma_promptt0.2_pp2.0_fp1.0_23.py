import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()

print(decompressor.decompress(data))

# Test LZMADecompressor.decompress() with multiple calls

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()

chunks = []
chunk_size = 1024
for i in range(0, len(data), chunk_size):
    chunks.append(decompressor.decompress(data[i:i+chunk_size]))

print(''.join(chunks))

# Test LZMADecompressor.decompress() with multiple calls and extra data

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()

chunks = []
chunk_
