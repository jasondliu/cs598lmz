import lzma
# Test LZMADecompressor.decompress()

def test_lzma_decompress_preliminary():
    assert lzma.decompress(BLANK_MAGIC) == b''
    assert lzma.decompress(b'\xFD7zXZ\x00') == b''

    assert (
        lzma.decompress(b'\xFD7zXZ\x00\x00\x00\x00\x04\x00\x02F'
                      + b(b'\xF3\x80\x31\x01'))
        == b'ab'
        )
    decomp = lzma.LZMADecompressor()
    buf = b''
