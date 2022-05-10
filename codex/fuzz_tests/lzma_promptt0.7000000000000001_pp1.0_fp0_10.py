import lzma
# Test LZMADecompressor:
decomp = lzma.LZMADecompressor()
with open('lzma_compressed.txt', 'rb') as f:
    file_content = f.read()

with open('lzma_compressed.txt', 'rb') as f:
    file_content = decomp.decompress(f.read())
    print(file_content)

# Test LZMACompressor:
comp = lzma.LZMACompressor()
with open('lzma_decompressed.txt', 'wb') as f:
    f.write(comp.compress(b'This is a test'))
    f.write(comp.flush())

with open('lzma_decompressed.txt', 'rb') as f:
    file_content = decomp.decompress(f.read())
    print(file_content)

# Test LZMAFile:
with lzma.open('lzma_compressed.txt', 'rb') as f:
    print(f.read())

with lzma.open('
