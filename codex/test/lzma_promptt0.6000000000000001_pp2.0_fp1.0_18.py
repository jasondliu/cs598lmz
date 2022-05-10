import lzma
# Test LZMADecompressor and LZMACompressor

def test_comp_decomp():
    data = b'This is the original text.'
    comp = LZMACompressor()
    cdata = comp.compress(data)
    cdata += comp.flush()
    decomp = LZMADecompressor()
    ddata = decomp.decompress(cdata)
    assert ddata == data
    assert not decomp.unused_data

def test_unused_data():
    data = b'This is the original text.'
    comp = LZMACompressor()
    cdata = comp.compress(data)
    cdata += comp.flush()
    decomp = LZMADecompressor()
    ddata = decomp.decompress(cdata, max_length=10)
    assert ddata == data[:10]
    assert decomp.unused_data == data[10:]

def test_decompress_error():
    data = b'This is the original text.'
    comp = LZMACompressor()
