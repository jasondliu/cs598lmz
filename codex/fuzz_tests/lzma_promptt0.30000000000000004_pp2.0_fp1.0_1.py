import lzma
# Test LZMADecompressor
comp = lzma.LZMACompressor()
data = comp.compress(b"Hello world!")
data += comp.flush()
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# Test LZMADecompressor.decompress() with a bad input
decomp = lzma.LZMADecompressor()
try:
    decomp.decompress(b"")
except EOFError:
    pass

# Test LZMADecompressor.decompress() with a truncated input
decomp = lzma.LZMADecompressor()
try:
    decomp.decompress(data[:-1])
except EOFError:
    pass

# Test LZMADecompressor.decompress() with a bad input
decomp = lzma.LZMADecompressor()
try:
    decomp.decompress(b"\x00")
except lzma.LZMAError:
    pass

# Test LZMAD
