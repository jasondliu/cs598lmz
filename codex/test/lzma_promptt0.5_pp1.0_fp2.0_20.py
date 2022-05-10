import lzma
# Test LZMADecompressor

def test_lzmadecompressor_read():
    data = b"Hello World"
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.read(len(data)) == b""
    d.decompress(cdata)
    assert d.read(len(data)) == data


def test_lzmadecompressor_read_chunks():
    data = b"Hello World"
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    for i in range(len(cdata)):
        d.decompress(cdata[i:i+1])
    assert d.read(len(data)) == data


def test_lzmadecompressor_readline():
    data = b"Hello World"
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    assert d.readline() == b""
