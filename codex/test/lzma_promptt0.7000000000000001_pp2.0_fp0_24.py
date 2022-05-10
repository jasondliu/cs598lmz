import lzma
# Test LZMADecompressor.flush()
data = lzma.compress(b"test") + b"\1"
dec = lzma.LZMADecompressor()
dec.decompress(data)
