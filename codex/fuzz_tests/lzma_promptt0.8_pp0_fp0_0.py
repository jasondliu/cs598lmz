import lzma
# Test LZMADecompressor.decompress() and LZMADecompressor.flush()
comp = lzma.LZMACompressor()
print(comp.compress(b"foo"))
print(comp.flush())

dec = lzma.LZMADecompressor()
print(dec.decompress(b"\xf3o\x03\x00\x00\x00\x00\x00\x01\x00"))
print(dec.flush())

# Test LZMADecompressor.decompress() and LZMADecompressor.flush()
dec = lzma.LZMADecompressor()
print(dec.decompress(b"\xf3o\x03\x00\x00\x00\x00\x00\x01\x00"))
print([dec.eof, dec.unused_data])
print(dec.flush())
print([dec.eof, dec.unused_data])

# Test LZMADecompressor.decompress() and LZMADecompressor.flush
