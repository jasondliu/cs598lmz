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

def test_utf8_decoder():
    data = b'a\xc3\xa2\xe2\x82\xac'
    assert data.decode('utf-8', 'strict') == u'a\xe2\x82\xac'
    assert data.decode('utf-8', 'replace') == u'a\ufffd\ufffd'
    assert data.decode('utf-8', 'ignore') == u'a'

    assert data.decode('utf-8', 'backslashreplace') == u'a\\u00e2\\u20ac'
    assert data.decode('utf-8', 'xmlcharrefreplace') == u'a&#226;&#8364;'

    assert data.decode('utf-8', 'add_one_codepoint') == u'aa\xe2\x82\xac'
    assert data.decode('utf-8', 'add_utf16_bytes') == u'aab\ufffd'
    assert data.decode('utf-8', 'add_utf32
