import lzma
# Test LZMADecompressor with a chunk of data
decompressor = lzma.LZMADecompressor()
data = b'this is the original data'
compressed = decompressor.compress(data)
print('compressed:', len(compressed), compressed)
print('decompressed:', decompressor.decompress(compressed))

print('decompressed:', decompressor.decompress(compressed, max_length=9))
print('decompressed:', decompressor.decompress(compressed, max_length=16))

# Test LZMAFile
with lzma.open('lzma_file.lzma', 'w') as f:
    f.write(data)

with lzma.open('lzma_file.lzma', 'r') as f:
    print('read:', f.read())

with lzma.open('lzma_file.lzma', 'r') as f:
    print('read:', f.read(9))
    print('read:', f.read(9))
    print
