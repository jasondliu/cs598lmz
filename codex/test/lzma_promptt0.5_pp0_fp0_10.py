import lzma
# Test LZMADecompressor.decompress.
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test LZMADecompressor.__init__.
with lzma.open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
