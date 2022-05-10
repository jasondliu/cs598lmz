import lzma
# Test LZMADecompressor creation

def test_decompress_stop_after_header():
    inp = BytesIO()

    with pytest.raises(lzma.LZMAError) as excinfo:
        lzdecomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, stop_after_header=True)
        decomp = lzdecomp.decompress(inp.read())
        assert decomp == b''

    assert str(excinfo.value) == 'Not a valid XZ header'

    inp = BytesIO(b'\xfd\x37\x7a\x58\x5a\x00')

    with pytest.raises(lzma.LZMAError) as excinfo:
        lzdecomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, stop_after_header=True)
        decomp = lzdecomp.decompress(inp.read())
        assert decomp == b''

    assert str(excinfo.
