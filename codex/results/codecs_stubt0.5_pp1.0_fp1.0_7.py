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

def test_utf_16_be_decoder():
    assert codecs.utf_16_be_decode(b'\xfe\xff\x00\x61\x00\x62\x00\x63', 'replace') == ('abc', 4)
    assert codecs.utf_16_be_decode(b'\xfe\xff\x00\x61\x00\x62\x00\x63', 'ignore') == ('abc', 6)
    assert codecs.utf_16_be_decode(b'\xfe\xff\x00\x61\x00\x62\x00\x63', 'backslashreplace') == ('\\u0061\\u0062\\u0063', 8)
    assert codecs.utf_16_be_decode(b'\xfe\xff\x00\x61\x00\x62\x00\x63', 'xmlcharrefreplace') == ('&#x61;&#x62;&#x63;', 8)
    assert codecs.utf_16_
