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

compressor = lzma.LZMAEncoder()

with open('test.xz', 'wb') as f:
    f.write(compressor.compress(b'Hello'))
    f.write(compressor.compress(b'World'))
    f.write(compressor.compress(b''))
    f.write(compressor.compress(b'!'))

# Test LZMAFile

with lzma.open('test.xz', 'wb') as f:
    f.write(b'Hello')
    f.write(b'World')
    f.write(b
