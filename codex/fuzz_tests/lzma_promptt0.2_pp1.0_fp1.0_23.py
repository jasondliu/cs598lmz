import lzma
# Test LZMADecompressor

with lzma.open('data/lzma/lzma_compressed.txt.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('data/lzma/lzma_compressed.txt', 'rb') as input:
    with lzma.open('data/lzma/lzma_compressed.txt.xz', 'wb') as output:
        output.write(compressor.compress(input.read()))
        output.write(compressor.flush())

# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with lzma.open('data/lzma/lzma_compressed.txt.xz') as input:
    with open('data/lzma/lzma_decompressed.txt', 'wb') as output:
        while True:
            chunk = input.
