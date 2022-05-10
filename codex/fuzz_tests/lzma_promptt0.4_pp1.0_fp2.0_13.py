import lzma
# Test LZMADecompressor

with lzma.open('data/lzma_file.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('data/lzma_file.xz', 'wb') as f:
    f.write(compressor.compress(b"Hello world!"))
    f.write(compressor.flush())
