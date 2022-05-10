import lzma
# Test LZMADecompressor
# with open('lzma_compressed_file', 'rb') as f:
#     decompressor = lzma.LZMADecompressor()
#     data = f.read()
#     result = decompressor.decompress(data)
#     print(result)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('lzma_compressed_file', 'wb') as f:
    f.write(compressor.compress(b'This is a test'))
    f.write(compressor.compress(b'of the LZMA compression'))
    f.write(compressor.compress(b'and decompression'))
    f.write(compressor.compress(b'algorithms.'))
    f.write(compressor.flush())
