import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"garbage")
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"")
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"\x00")
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"\x00" * 10)
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"\x00" * (lzma.CHECK_SIZE + 1))
    with pytest.raises(lzma.LZMAError):
        c.decompress(b"\x00" * lzma.CHECK_SIZE)
    with pytest.raises(lzma.LZ
