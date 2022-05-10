import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    file_content = f.read()
    data = compressor.decompress(file_content)
    print(data)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('test.xz', 'wb') as f:
    f.write(compressor.compress(b"Hello world!"))
    f.write(compressor.flush())

# Test LZMAFile
with lzma.open('test.xz', 'wt') as f:
    f.write("Hello world!")

with lzma.open('test.xz', 'rt') as f:
    print(f.read())

# Test LZMAError
try:
    with lzma.open('test.xz', 'rt') as f:
        f.read()
except lzma.LZMAError as e:
    print(e)

# Test LZMA
