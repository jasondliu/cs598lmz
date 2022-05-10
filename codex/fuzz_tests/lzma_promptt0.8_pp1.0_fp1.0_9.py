import lzma
# Test LZMADecompressor, LZMAFile

def test_encode_decode():
    data = 'data' * 100000
    cdata = lzma.compress(data)
    data2 = lzma.decompress(cdata)
    assert data == data2

def test_compress_nonblock_size():
    data = 'data' * 100000
    cdata = lzma.compress(data, format=lzma.FORMAT_ALONE)
    cdata2 = lzma.compress(data, format=lzma.FORMAT_XZ,
                           check=lzma.CHECK_CRC64, filters=[{"id": lzma.FILTER_LZMA1, "preset": 9 | lzma.PRESET_EXTREME}])
    assert len(cdata2) < len(cdata)

def test_filter_specs():
    data = 'data' * 100000
    cdata = lzma.compress(data, format=lzma.FORMAT_ALONE, filters=[{"id": l
