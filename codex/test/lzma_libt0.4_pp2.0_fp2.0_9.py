import lzma
lzma.LZMAError

#
# LZMADecompressor
#

def test_LZMADecompressor_decompress():
    # test decompress()
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""
    assert c.decompress(b"\x00") == b"\x00"
    assert c.decompress(b"\x00\x00") == b"\x00\x00"
    assert c.decompress(b"\x00\x00\x00") == b"\x00\x00\x00"
    assert c.decompress(b"\x00\x00\x00\x00") == b"\x00\x00\x00\x00"
    assert c.decompress(b"\x00\x00\x00\x00\x00") == b"\x00\x00\x00\x00\x00"
