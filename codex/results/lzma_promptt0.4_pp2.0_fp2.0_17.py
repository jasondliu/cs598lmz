import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
with gzip.open('/tmp/test.gz', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    print(data)

# Test LZMAFile
with lzma.open('/tmp/test.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile
with lzma.open('/tmp/test.xz', 'wt') as f:
    f.write('hello world!')

# Test LZMAFile
with lzma.open('/tmp/test.xz', 'rt') as f:
    file_content = f.read()
    print(file_content)
