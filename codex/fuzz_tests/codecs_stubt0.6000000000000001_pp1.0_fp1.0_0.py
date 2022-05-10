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

def test_unicode_escape():
    # test unicode_escape
    assert codecs.escape_decode(r'\u20ac\U000020ac') == (b'\xe2\x82\xac\xe2\x82\xac', 6)
    assert codecs.escape_decode(r'\u20ac\U000020ac', 'strict') == (b'\xe2\x82\xac\xe2\x82\xac', 6)
    assert codecs.escape_decode(r'\u20ac\U000020ac', 'replace') == (b'?\xe2\x82\xac', 6)
    assert codecs.escape_decode(r'\u20ac\U000020ac', 'ignore') == (b'\xe2\x82\xac', 6)
    assert codecs.escape_decode(r'\u20ac\U000020ac', 'add_one_codepoint') == (b'a\xe2\x82\xac', 6)
    assert codec
