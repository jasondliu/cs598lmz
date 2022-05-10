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

def test_add_utf16_bytes():
    # Issue #1248
    assert codecs.decode(b'\xff\xfe\x00\x00', "utf-16", "add_utf16_bytes") == 'a\x00'
    assert codecs.decode(b'\xfe\xff\x00\x00', "utf-16-be", "add_utf16_bytes") == 'a\x00'
    assert codecs.decode(b'\xff\xfe', "utf-16", "add_utf16_bytes") == 'a'
    assert codecs.decode(b'\xfe\xff', "utf-16-be", "add_utf16_bytes") == 'a'

def test_add_utf32_bytes():
    # Issue #1248
    assert codecs.decode(b'\xff\xfe\x00\x00\x00\x00', "utf-32", "add_utf32_bytes") == 'a\x00\x00'
    assert codecs.dec
