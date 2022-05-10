import lzma
# Test LZMADecompressor
def test_lzma_decompressor():
    # Test decompressor
    decomp = lzma.LZMADecompressor()
    assert decomp.eof is False
    assert decomp.unused_data == b""
    assert decomp.decompress(b"") == b""
    assert decomp.unused_data == b""
    assert decomp.eof is False
    assert decomp.decompress(b"\x00") == b""
    assert decomp.unused_data == b"\x00"
    assert decomp.eof is False
    assert decomp.decompress(b"\x00" * 4) == b""
    assert decomp.unused_data == b"\x00" * 4
    assert decomp.eof is False
    assert decomp.decompress(b"\x00" * 5) == b"\x00"
    assert decomp.unused_data == b"\x00" * 4
    assert decomp.eof is False
    assert decomp.decompress(b"\x00" * 5) == b""

