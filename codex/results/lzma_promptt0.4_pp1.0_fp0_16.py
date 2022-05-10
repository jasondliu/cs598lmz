import lzma
# Test LZMADecompressor.decompress()

def test_decompress_simple():
    # This test was taken from the original LZMA SDK.
    compressed = b'\x5d\x00\x00\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\x00'
    uncompressed = b'Hello, world!'
    dc = lzma.LZMADecompressor()
    assert dc.decompress(compressed) == uncompressed
    assert dc.unused_data == b''
    assert dc.eof is True

def test_decompress_eof():
    # This test was taken from the original LZMA SDK.
    compressed = b'\x5d\x00\x00\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\
