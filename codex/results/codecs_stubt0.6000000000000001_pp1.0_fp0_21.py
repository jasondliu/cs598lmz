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

def check_utf8(encoding):
    # Check that utf-8 is detected and handled correctly.
    assert codecs.utf_8_decode('\xed\xa0\x80', errors='replace') == (
        u'\ufffd', 2)
    assert codecs.utf_8_decode('\xed\xa0\x80', errors='ignore') == (
        u'', 0)
    assert codecs.utf_8_decode('\xed\xa0\x80', errors='backslashreplace') == (
        u'\\U0010ffff', 2)

    assert codecs.utf_8_decode('\xed\xa0\x80', errors='xmlcharrefreplace') == (
        u'&#65533;', 2)
    assert codecs.utf_8_decode('\xed\xa0\x80', errors='surrogateescape') == (
        u'\udc80', 2)
    assert codecs.utf_8_decode('\xed\xa0\x80', errors
