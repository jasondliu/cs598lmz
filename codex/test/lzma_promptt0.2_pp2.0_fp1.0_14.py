import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    file_content = f.read()

decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(file_content)
print(result)

# Test LZMAFile
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
print(file_content)

# Test LZMAFile with mode='w'
with lzma.open('test.xz', 'w') as f:
    f.write(b'Hello World!')

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
print(file_content)

# Test LZMAFile with mode='a'
with lzma.open('test.xz', 'a') as f:
    f.write(b' Goodbye!')

