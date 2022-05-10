import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    with lzma.LZMADecompressor() as d:
        assert d.decompress(data) == b''
        assert d.unused_data == data
        assert d.eof == False

        assert d.decompress(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') == b'\x00'
        assert d.unused_data == b''
        assert d.eof == False

        assert d.decompress(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
