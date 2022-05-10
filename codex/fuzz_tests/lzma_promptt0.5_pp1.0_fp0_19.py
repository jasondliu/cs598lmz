import lzma
# Test LZMADecompressor
lzma_decompressor = lzma.LZMADecompressor()
decompressed_data = lzma_decompressor.decompress(compressed_data)
len(decompressed_data)

# Test LZMACompressor
lzma_compressor = lzma.LZMACompressor()
compressed_data = lzma_compressor.compress(data)
compressed_data += lzma_compressor.flush()
len(compressed_data)
