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

def test_utf8(encoding):
    # Test UTF-8
    assert codecs.decode(b'\xc3\xa9', encoding) == '\xe9'
    assert codecs.decode(b'\xe2\x82\xac', encoding) == '\u20ac'
    assert codecs.decode(b'\xf0\x90\x8c\xbc', encoding) == '\U00010cbc'
    assert codecs.decode(b'\xf4\x8f\xbf\xbf', encoding) == '\U0010ffff'

    assert codecs.decode(b'\xc3\xa9', encoding, 'strict') == '\xe9'
    assert codecs.decode(b'\xe2\x82\xac', encoding, 'strict') == '\u20ac'
    assert codecs.decode(b'\xf0\x90\x8c\xbc', encoding, 'strict') == '\U00010cbc'
    assert codecs.dec
