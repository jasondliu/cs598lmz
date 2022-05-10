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

def test_add_one_codepoint(encoding):
    u = u'\u1234'
    b = u.encode(encoding)
    assert b.decode(encoding, "add_one_codepoint") == u'a\u1234'

def test_add_utf16_bytes(encoding):
    u = u'\u1234'
    b = u.encode(encoding)
    assert b.decode(encoding, "add_utf16_bytes") == u'ab\u1234'

def test_add_utf32_bytes(encoding):
    u = u'\u1234'
    b = u.encode(encoding)
    assert b.decode(encoding, "add_utf32_bytes") == u'abcd\u1234'

def test_utf8_surrogates(encoding):
    u = u'\U00012345'
    b = u.encode(encoding)
    assert b.decode(encoding, "add_one
