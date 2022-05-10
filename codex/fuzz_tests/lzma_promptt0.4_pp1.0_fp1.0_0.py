import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    with lzma.open(BytesIO(testdata_lzma), "r") as f:
        assert f.read() == testdata_compressed

def test_LZMADecompressor_buffer_size():
    with lzma.open(BytesIO(testdata_lzma), "r", buffer_size=1) as f:
        assert f.read() == testdata_compressed

def test_LZMADecompressor_invalid_data():
    with raises(lzma.LZMAError):
        lzma.LZMADecompressor().decompress(b"invalid")

def test_LZMADecompressor_unused_data():
    with raises(lzma.LZMAError):
        lzma.LZMADecompressor().decompress(testdata_compressed + b"unused")

def test_LZMADecompressor_unused_data_eof():
    with raises(lz
