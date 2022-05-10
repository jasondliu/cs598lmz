import lzma
# Test LZMADecompressor
def test_lzma_decompressor():
    data = b'\xfd7zXZ\x00' + lzma.compress(b'1234567890')
    f = io.BytesIO(data)
    with lzma.open(f, "rb") as lz:
        assert lz.read() == b'1234567890'
    with lzma.open(f, "rb") as lz:
        assert lz.read(5) == b'12345'
        assert lz.read(5) == b'67890'
    with lzma.open(f, "rb") as lz:
        assert lz.read(None) == b'1234567890'
    with lzma.open(f, "rb") as lz:
        assert lz.read1(5) == b'12345'
        assert lz.read1(5) == b'67890'
    with lzma.open(f, "rb") as lz:
        assert lz.read1(None)
