import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "rb") as f:
        data = f.read()
    with lzma.open(TESTFN, "rb") as f:
        f.seek(0)
        decomp = lzma.LZMADecompressor()
        assert decomp.eof is False
        assert decomp.unused_data == b""
        assert decomp.decompress(b"") == b""
        assert decomp.unused_data == b""
        assert decomp.decompress(b"garbage") == b""
        assert decomp.unused_data == b"garbage"
        assert decomp.decompress(b"") == b""
        assert decomp.unused_data == b"garbage"
        assert decomp.decompress(f.read()) == data
        assert decomp.unused_data == b""
        assert decomp.eof is True
        assert decomp.decompress(b"garbage") == b""
        assert decomp.unused_data ==
