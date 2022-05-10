import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "rb") as f:
        decomp = lzma.LZMADecompressor()
        data = f.read(100)
        more = decomp.decompress(data)
        more += decomp.flush()
        more += decomp.decompress(f.read())
        assert more == DATA
        assert not decomp.unused_data
        assert not decomp.eof
        with pytest.raises(EOFError):
            decomp.decompress(b"")
        assert decomp.unused_data == b""
        assert decomp.eof

def test_lzma_decompressor_unused_data():
    with lzma.open(TESTFN, "rb") as f:
        decomp = lzma.LZMADecompressor()
        data = f.read(100)
        more = decomp.decompress(data, max_length=50)
        assert more == DATA[:50]
        assert decomp.un
