import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(data) == b'12345abcde'
    assert decomp.unused_data == b''
    assert decomp.eof is True
    assert decomp.decompress(b'blah') == b''
    assert decomp.unused_data == b'blah'
    assert decomp.eof is False
    assert decomp.decompress(b'blah', max_length=2) == b'12'
    assert decomp.unused_data == b'345abcde'
    assert decomp.eof is False
    assert decomp.decompress(b'blah', max_length=20) == b'345abcde'
