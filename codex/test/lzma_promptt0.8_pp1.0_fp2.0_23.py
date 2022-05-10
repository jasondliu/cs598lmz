import lzma
# Test LZMADecompressor.__call__() with a series of valid and invalid
# parameters.

def test_decompress():
    for b in [b'', b'a', b'ab', b'abc']:
        decomp = lzma.LZMADecompressor()
        assert decomp(b) == b
        with pytest.raises(TypeError):
            decomp(memoryview(b))
        with pytest.raises(TypeError):
            decomp(array.array('B', b))
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(b'abc') == b''
    assert decomp.decompress(b'abc', max_length=1) == b'a'
    with pytest.raises(MemoryError):
        decomp.decompress(b'abc', max_length=0)
    assert decomp.unconsumed_tail == []
    with pytest.raises(RuntimeError):
        decomp.decompress(b'abc', max_length=1)
