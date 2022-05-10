import lzma
# Test LZMADecompressor with a few bytes of input


def test_lzma_decompressor_small_input():
    c = lzma.LZMADecompressor()
    assert c.decompress(b'') == b''
    assert c.decompress(b'\x00') == b''
    assert c.decompress(b'\x00' * 100) == b''
# Test LZMADecompressor on corrupted data


def test_lzma_decompressor_truncated_input():
    c = lzma.LZMADecompressor()
    with pytest.raises(lzma.LZMAError) as excinfo:
        c.decompress(b'\x00' * 5)
    # Cannot test the exact error message because it includes the address
    # of the LZMADecompressor object
    assert 'Input format not recognized' in str(excinfo)


def test_lzma_decompressor_corrupted_stream():
    c = lzma.LZMADecompressor()
