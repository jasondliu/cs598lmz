import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    with lzma.LZMADecompressor() as decomp:
        assert decomp.decompress(data) == b''
        assert decomp.unused_data == b''
        assert decomp.eof is False
        assert decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') == b''
        assert decomp.unused_data == b''
        assert decomp.eof is False
        assert decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
