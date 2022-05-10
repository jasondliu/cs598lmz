import lzma
# Test LZMADecompressor
def test_LZMADecompressor():
    c = lzma.LZMADecompressor()
    assert isinstance(c.decompress(b''), bytes)
    assert c.unused_data == b''
    assert c.eof is False
    assert c.decompress(b'\x00') == b''
    assert c.unused_data == b'\x00'
    assert c.eof is False
    # What follows is a xz-compressed, empty bytestring.
    xz_empty_string = (
        b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5"
        b"\xa3\x01\x00\x04")
    assert c.decompress(xz_empty_string) == b""
    assert c.unused_data == b""
    assert c.eof is True
    # The
