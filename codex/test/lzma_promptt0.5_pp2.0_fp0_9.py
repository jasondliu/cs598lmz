import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(os.path.join(os.path.dirname(__file__), 'data/lzma.xz'),
                   'rb') as f:
        data = f.read()
        assert len(data) == 5
        assert data == b'hello'

def test_lzma_decompressor_fileobj():
    with open(os.path.join(os.path.dirname(__file__), 'data/lzma.xz'),
              'rb') as f:
        with lzma.LZMADecompressor().stream(f) as d:
            data = d.read()
            assert len(data) == 5
            assert data == b'hello'

