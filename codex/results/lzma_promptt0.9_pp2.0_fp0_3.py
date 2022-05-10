import lzma
# Test LZMADecompressor with no input
def test_no_input():
    decomp = lzma.LZMADecompressor()
    with pytest.raises(EOFError):
        decomp.decompress(b'')
    with pytest.raises(ValueError):
        decomp.flush()

# Test LZMADecompressor with truncated input
def test_truncated_input():
    with pytest.raises(EOFError):
        lzma.decompress(COMPRESSED_NO_CHECK)
    with pytest.raises(lzma.LZMAError):
        lzma.decompress(COMPRESSED_CHECK)
    with pytest.raises(lzma.LZMAError):
        lzma.decompress(COMPRESSED_XZ)

# Test LZMADecompressor with clever input
def test_clever_input():
    decomp = lzma.LZMADecompressor()
    with pytest.raises(TypeError):
        decomp.decompress(None)

