import lzma
# Test LZMADecompressor with a garbage file.
# It should raise EOFError on decompression.
d = lzma.LZMADecompressor()
with pytest.raises(EOFError):
    d.decompress(b"garbage")
# Test LZMADecompressor with empty input.
# It should raise EOFError on decompression.
d = lzma.LZMADecompressor()
with pytest.raises(EOFError):
    d.decompress(b"")
# Test LZMADecompressor with an incomplete header.
# It should raise EOFError on decompression.
d = lzma.LZMADecompressor()
with pytest.raises(EOFError):
    d.decompress(b"\xfd7zXZ\x00")
# Test LZMADecompressor with a corrupt header.
# It should raise LZMAError on decompression.
d = lzma.LZMADecompressor()
with pytest.raises(lzma.LZMAError):
