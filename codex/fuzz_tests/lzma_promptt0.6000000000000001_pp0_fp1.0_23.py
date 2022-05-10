import lzma
# Test LZMADecompressor - decompress, flush, reset

def gen_data(n=10000):
    return b''.join(bytes([random.randint(0, 255)]) for i in range(n))

def test_read1(n=1000):
    data = gen_data(n)
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(cdata) == data
    assert d.unused_data == b''
    assert d.eof
    assert d.decompress(b'') == b''
    assert d.unused_data == b''
    assert d.eof

def test_read2(n=1000):
    data = gen_data(n)
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.decompress(cdata[:1]) == b''
    assert d.unused_data == cdata[:1]
    assert not d.e
