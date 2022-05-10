import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMACompressor
comp = lzma.LZMACompressor()
comp.compress(data)
comp.flush()

# Test LZMADecompressor.decompress
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMACompressor.compress
comp = lzma.LZMACompressor()
comp.compress(data)
comp.flush()

# Test LZMADecompressor.decompress
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMACompressor.compress
comp = lzma.LZMACompressor()
comp.compress(data)
comp.flush()

# Test LZMADecompressor.decompress
decomp = lzma.LZMADecompressor()
decomp.decomp
