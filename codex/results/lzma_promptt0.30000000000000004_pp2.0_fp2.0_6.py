import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "wb") as f:
        f.write(b"foo")
    with lzma.open(TESTFN, "rb") as f:
        decompressor = lzma.LZMADecompressor()
        assert decompressor.decompress(f.read()) == b"foo"
        assert decompressor.unused_data == b""
        assert decompressor.eof is True
        assert decompressor.decompress(b"garbage") == b""
        assert decompressor.unused_data == b"garbage"
        assert decompressor.eof is False
        assert decompressor.decompress(b"") == b""
        assert decompressor.unused_data == b"garbage"
        assert decompressor.eof is False
        assert decompressor.decompress(b"baz") == b""
        assert decompressor.unused_data == b"garbagebaz"
        assert decompressor.eof is False
        assert decomp
