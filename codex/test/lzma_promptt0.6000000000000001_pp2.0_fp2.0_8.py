import lzma
# Test LZMADecompressor with multiple calls to decompress().
# https://github.com/python/cpython/pull/7446
def test_lzma_multiple_calls_to_decompress(data):
    c = lzma.LZMADecompressor()
    assert c.decompress(data[:100]) == b''
    assert c.decompress(data[100:]) == b'hello\n'
    assert c.decompress(b'blah') == b''

def test_lzma_decompress_invalid_start_byte():
    c = lzma.LZMADecompressor()
    with pytest.raises(lzma.LZMAError) as excinfo:
        c.decompress(b'\x00')
    assert str(excinfo.value) == 'not an LZMA-compressed file'

def test_lzma_decompress_invalid_end_byte():
    c = lzma.LZMADecompressor()
