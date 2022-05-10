import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_utf16(encoding="utf-16"):
    # Test UTF-16 surrogate pair
    u = "\ud800\udc02"
    assert u.encode(encoding) == b'\x00\x02'
    assert u.encode(encoding, 'surrogatepass') == b'\x00\x02'
    assert u.encode(encoding, 'replace') == b'?'
    assert u.encode(encoding, 'ignore') == b''
    for exc in ('surrogateescape', 'add_utf16_bytes'):
        assert u.encode(encoding, exc) == b'\x00\x02'

    # Test UTF-16 surrogate pair with non-BMP character
    u = "\ud800\udc02\U00010000"
    assert u.encode(encoding) == b'\x00\x02\xd8\x00\xdc\x00'
    assert u.encode(encoding, 'surrogatepass') == b'\x00\x02\xd
