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
    # Test UTF-8
    assert codecs.utf_8_decode(b'\xed\xa0\x80') == ('\ud800', 2)
    assert codecs.utf_8_decode(b'\xed\xa0\x80', 'replace') == ('\ufffd', 2)
    assert codecs.utf_8_decode(b'\xed\xa0\x80', 'ignore') == ('', 2)
    assert codecs.utf_8_decode(b'\xed\xa0\x80', 'backslashreplace') == ('\\ud800', 2)
    assert codecs.utf_8_decode(b'\xed\xa0\x80', 'xmlcharrefreplace') == ('&#55296;', 2)
    assert codecs.utf_8_decode(b'\xed\xa0\x80', 'add_one_codepoint') == ('a\ud800', 3)
    assert codecs.utf_8_decode(b'\
