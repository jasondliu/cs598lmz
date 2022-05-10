import lzma
# Test LZMADecompressor

lzma_decompress = lzma.LZMADecompressor()

with open("../data/lzma/lzma_compress_test.bin", "rb") as f:
    data = f.read()

with open("../data/lzma/lzma_decompress_test.bin", "wb") as f:
    f.write(lzma_decompress.decompress(data))
    
# Test LZMAEncoder

lzma_compress = lzma.LZMAEncoder()

with open("../data/lzma/lzma_compress_test.bin", "wb") as f:
    f.write(lzma_compress.compress(b"Hello World"))

# Test LZMADecompressor

lzma_decompress = lzma.LZMADecompressor()

with open("../data/lzma/lzma_compress_test.bin", "rb") as f:
    data = f.
