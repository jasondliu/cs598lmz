import lzma
# Test LZMADecompressor

data = b'this is the data to compress'

compressor = lzma.LZMACompressor()
comp_data = compressor.compress(data)
comp_data += compressor.flush()

decompressor = lzma.LZMADecompressor()
decomp_data = decompressor.decompress(comp_data)

print(decomp_data)

