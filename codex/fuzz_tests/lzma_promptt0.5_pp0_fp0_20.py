import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
with open('lzma_compressed', 'rb') as f:
    compressed_data = f.read()
    data = decompressor.decompress(compressed_data)
    with open('lzma_decompressed', 'wb') as f:
        f.write(data)
 
# Test LZMACompressor and LZMADecompressor.
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
with open('lzma_decompressed', 'rb') as f:
    data = f.read()
    compressed_data = compressor.compress(data)
    compressed_data += compressor.flush()
    with open('lzma_compressed2', 'wb') as f:
        f.write(compressed_data)
    print(compressed_data)
    decompressed_data = decompressor.decompress(compressed_data)
    with open('lzma_decomp
