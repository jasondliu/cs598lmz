import lzma
# Test LZMADecompressor


def roundtrip(s, algorithms='xz', filters=None):
    if sys.version_info >= (2, 7):
        assert lzma.decompress(lzma.compress(s, algo=algorithms,
            filters=filters)) == s
    else:
        assert lzma.decompress(lzma.compress(s)) == s

def roundtrip_file(fname):
    if sys.version_info >= (2, 7):
        with open(fname, 'rb') as f:
            data = f.read()
        assert lzma.decompress(lzma.compress(data, format=lzma.FORMAT_XZ),
            format=lzma.FORMAT_AUTO) == data
    else:
        assert lzma.decompress(lzma.compress(data)) == data

def test_decomp():
    c = lzma.LZMADecompressor()
    assert c.needs_input == False

    assert c.eof ==
