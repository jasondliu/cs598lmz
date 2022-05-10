import lzma
# Test LZMADecompressor with a small input buffer.
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"x") == b"foo"
assert decomp.decompress(b"") == b"foo"
assert decomp.decompress(b"bar") == b"\x82"
assert decomp.decompress(b"a", 10) == b"" # 10 is ignored
# check that remaining in the stream is retained if not decompressed
lzc = lzma.LZMACompressor()
comp = lzc.compress(b"foo")
comp += lzc.flush()
comp += lzc.compress(b"bar")
comp += lzc.flush()
dec = lzma.LZMADecompressor()
l = len(comp)
b = bytearray(2)
s = 0
stream = dec.decompress(comp[s:s+l])
stream += dec.flush()
assert dec.eof == 1
s += l
l = len(comp) - s
assert stream == b
