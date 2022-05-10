import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    file_content = f.read()

decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(file_content)

with open('test.txt', 'wb') as f:
    f.write(result)
 
# Test LZMAFile
with lzma.open('test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile
with lzma.open('test.xz') as f:
    file_content = f.readlines()
    print(file_content)

# Test lzma.open with mode='w'
with lzma.open('test.xz', mode='w') as f:
    f.write(b"1234567890")

with lzma.open('test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile
