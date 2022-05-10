import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
d

# Test LZMADecompressor.decompress()
d.decompress(b"Hello, World!")

d.decompress(b"")
d.decompress(b"Hello, World!", max_length=5)

d.eof

# Test LZMADecompressor.unconsumed_tail
d.unconsumed_tail
d.decompress(b"Hello, World!")
d.unconsumed_tail

# Test LZMADecompressor()
d = lzma.LZMADecompressor()
d.decompress(b"Hello, World!")

d = lzma.LZMADecompressor()
with pytest.raises(ValueError):
    d.decompress(b"Hello, World!", max_length=-1)

d = lzma.LZMADecompressor()
with pytest.raises(lzma.LZMAError):
    d.dec
