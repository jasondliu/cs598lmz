import lzma
# Test LZMADecompressor

def test_LZMADecompressor_read():
    with lzma.open(TESTFN, "w") as f:
        f.write(b"1234567890" * 1000)

    with lzma.open(TESTFN, "r") as f:
        d = lzma.LZMADecompressor()
        data = f.read(100)
        assert d.decompress(data) == b"1234567890" * 10
        data = f.read(100)
        assert d.decompress(data) == b"1234567890" * 10
        data = f.read(1000)
        assert d.decompress(data) == b"1234567890" * 100
        data = f.read()
        assert d.decompress(data) == b"1234567890" * 900
        assert d.unused_data == b""
        assert d.eof == True
        assert f.read() == b""
        assert d.decompress(b"") == b""
        assert
