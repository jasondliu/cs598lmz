import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

# Test LZMADecompressor.decompress(chunk)
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed[:100])
decompressor.decompress(compressed[100:])

# Test LZMADecompressor.flush()
decompressor.flush()

# Test LZMADecompressor.copy()
copy = decompressor.copy()
copy.decompress(compressed)

# Test LZMADecompressor.getstate()
state = decompressor.getstate()
decompressor.decompress(compressed)
decompressor.setstate(state)
decompressor.decompress(compressed)

# Test LZMADecompressor.getstate() for decompressors that have not
# been used yet.
state = decompressor.getstate()
decompressor.setstate(state)
decomp
