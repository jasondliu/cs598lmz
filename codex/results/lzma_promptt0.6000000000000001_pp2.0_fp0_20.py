import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMADecompressor with max_length
decomp = lzma.LZMADecompressor(max_length=len(data) + 100)
decomp.decompress(data)

# Test LZMADecompressor with max_length and dict_size
decomp = lzma.LZMADecompressor(max_length=len(data) + 100, dict_size=0x100)
decomp.decompress(data)

# Test LZMADecompressor.decompress with max_length
decomp = lzma.LZMADecompressor()
decomp.decompress(data, max_length=len(data) + 100)

# Test LZMADecompressor.decompress with max_length and dict_size
decomp = lzma.LZMADecompressor()
decomp.decompress(data, max_length=len(data) +
