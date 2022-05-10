import lzma
# Test LZMADecompressor with various data

def test_lzma_errors():
    lzma_decompressor = lzma.LZMADecompressor()
    for s in ['', 'x', 'x'*10, 'x'*1000]:
        yield check_error, lzma_decompressor, s

def check_error(decompressor, data):
    try:
        decompressor.decompress(data)
    except IOError:
        pass
    else:
        raise AssertionError("IOError not raised")

def test_lzma_decompress():
    lzma_decompressor = lzma.LZMADecompressor()
    data = lzma_decompressor.decompress(lzma_test_data)
    assert data == lzma_test_data_uncompressed

def test_lzma_decompress_non_stream():
    lzma_decompressor = lzma.LZMADecompressor()
    lzma_decompressor.decompress(
