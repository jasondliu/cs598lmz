import lzma
# Test LZMADecompressor

with lzma.open('/Users/michael/Downloads/test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor

compressor = lzma.LZMACompressor()
with open('/Users/michael/Downloads/test.xz', 'wb') as f:
    f.write(compressor.compress(b'hello world'))
    f.write(compressor.flush())
 
# Test LZMAFile

with lzma.open('/Users/michael/Downloads/test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile

with lzma.open('/Users/michael/Downloads/test.xz', 'w') as f:
    f.write(b'hello world')

# Test LZMAFile

with lzma.open('/Users/michael/Downloads/test.xz') as f:
