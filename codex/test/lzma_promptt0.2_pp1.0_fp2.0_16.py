import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression of a file
    with open('test/testdata/lzma.xz', 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        data = f.read()
        assert decompressor.decompress(data) == b"Hello world!\n"
        assert decompressor.unused_data == b""
        assert decompressor.eof is True
        assert decompressor.decompress(b"garbage") == b""
        assert decompressor.unused_data == b"garbage"
        assert decompressor.eof is False
        assert decompressor.decompress(b"") == b""
        assert decompressor.unused_data == b"garbage"
        assert decompressor.eof is False
        assert decompressor.decompress(b"garbage", max_length=5) == b"garba"
        assert decompressor.unused_data == b"ge"
        assert decompressor.eof is False
        assert decomp
