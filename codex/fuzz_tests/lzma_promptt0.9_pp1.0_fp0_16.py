import lzma
# Test LZMADecompressor.eof.

data = list(range(10000))
comp = lzma.LZMACompressor()
comp_data = comp.compress(bytes(data))
comp_data += comp.flush()
del comp

decomp = lzma.LZMADecompressor()
assert not decomp.eof
assert decomp.decompress(comp_data) == bytes(data)
for c in (b'a', b'', b'abc'):
    assert decomp.eof
    with pytest.raises(EOFError):
        decomp.decompress(c)
del decomp
# Test len(filter_properties).

def test_len_filter_properties():
    fp = lzma._lzma.FilterProperties()
    assert len(fp) == 1

    fp = lzma._lzma.FilterProperties([
        (lzma._lzma.FILTER_LZMA2, lzma._lzma.FILTER_DECOMPRESS, None),
    ])
    assert len(fp) == 1


