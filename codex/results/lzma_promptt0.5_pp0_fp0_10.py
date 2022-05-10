import lzma
# Test LZMADecompressor.decompress.
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test LZMADecompressor.__init__.
with lzma.open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    file_content = decompressor.decompress(f.read())
    print(file_content)

# Test LZMADecompressor.decompress_chunk.
with lzma.open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    file_content = b''
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        file_content += decompressor.decompress(chunk)
    file_content += decompressor.flush()
    print(file_content)

# Test LZMADecompressor.decompress
