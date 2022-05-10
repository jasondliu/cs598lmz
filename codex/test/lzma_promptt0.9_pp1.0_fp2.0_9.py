import lzma
# Test LZMADecompressor with a broken stream
def test_broken_stream():
    decompressor = lzma.LZMADecompressor()
    data = b'\x00\x00\x00\x00\xff'
    # Check that we raise an exception for truncated input
    raises(lzma.LZMAError, decompressor.decompress, data)
    # Run the decompressor to ensure it keeps state and raises an
    # exception on a second run
    raises(lzma.LZMAError, decompressor.decompress, b'')

def test_unknown_filters():
    stream = [{'id': lzma.FILTER_LZMA1, 'preset': 9 | lzma.PRESET_EXTREME}]
    raises(lzma.LZMAError, lzma.compress, b'some data', format=lzma.FORMAT_RAW,
           filters=stream)
