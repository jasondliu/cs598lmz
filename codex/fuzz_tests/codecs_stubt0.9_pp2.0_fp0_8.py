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

def test_add_codepoint():
    assert u'abc'.encode('utf-16', 'add_one_codepoint') == b'\xff\xfeb\x00a\x00c\x00'

def test_add_utf16():
    assert u'a'.encode('utf-8', 'add_utf16_bytes') == b'ab'
    assert u'a'.encode('utf-16', 'add_utf16_bytes') == b'\xff\xfeab\x00'
    assert u'a'.encode('utf-32', 'add_utf16_bytes') == b'\x00\x00\xfe\xffab\x00\x00\x00'

def test_add_utf32():
    assert u'a'.encode('utf-8', 'add_utf32_bytes') == b'\xc4\x80'
    assert u'a'.encode('utf-16', 'add_utf32_bytes') == b'\xdc\x00\x00\xdca\x00
