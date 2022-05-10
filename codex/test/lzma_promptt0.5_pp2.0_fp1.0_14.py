import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    file_content = f.read()
    result = c.decompress(file_content)
    print(result)

# Test LZMACompressor
c = lzma.LZMACompressor()
with open('test.xz', 'wb') as f:
    f.write(c.compress(b'1234567890'))
    f.write(c.flush())

# Test LZMAFile
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

with lzma.open('test.xz', 'wb') as f:
    f.write(b'1234567890')

# Test LZMAError
try:
    lzma.LZMAError()
except Exception as e:
    print(e)
