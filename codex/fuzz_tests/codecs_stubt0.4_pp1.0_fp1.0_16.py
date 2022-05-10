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

def test_main():
    # UTF-8
    assert u'\u20ac'.encode('utf-8', 'strict') == b'\xe2\x82\xac'
    assert u'\u20ac'.encode('utf-8', 'replace') == b'?'
    assert u'\u20ac'.encode('utf-8', 'ignore') == b''
    assert u'\u20ac'.encode('utf-8', 'xmlcharrefreplace') == b'&#8364;'
    assert u'\u20ac'.encode('utf-8', 'backslashreplace') == b'\\u20ac'
    assert u'\u20ac'.encode('utf-8', 'add_one_codepoint') == b'a\xe2\x82\xac'
    assert u'\u20ac'.encode('utf-8', 'add_utf16_bytes') == b'ab\xe2\x82\xac'
    assert u'\u20ac'.encode('utf-8', 'add
