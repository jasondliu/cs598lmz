import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAEncoder

