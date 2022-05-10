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

def test_utf8_surrogates():
    # Test surrogates in UTF-8
    assert codecs.utf_8_decode(b'\xed\xa0\x80') == (u'\ud800', 3)
    assert codecs.utf_8_decode(b'\xed\xa0\x81') == (u'\ud801', 3)
    assert codecs.utf_8_decode(b'\xed\xbf\xbf') == (u'\udfff', 3)
    assert codecs.utf_8_decode(b'\xed\xa0\x80\xed\xa0\x81', "replace") == (
        u'\ud800\ud801', 6)
    assert codecs.utf_8_decode(b'\xed\xa0\x80\xed\xa0\x81', "ignore") == (
        u'', 6)
    assert codecs.utf_8_decode(b'\xed\xa0\x80\xed\xa0
