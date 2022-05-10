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

# test the codecs module

def test_codecs():
    # test the builtin UTF-8 codec
    assert codecs.utf_8_encode(u"abc") == (b"abc", 3)
    assert codecs.utf_8_encode(u"abc\u20ac") == (b"abc\xe2\x82\xac", 7)
    assert codecs.utf_8_encode(u"\U00012345") == (b"\xf0\x92\x8d\x85", 4)
    assert codecs.utf_8_encode(u"\U0007ffff") == (b"\xef\xbf\xbf", 3)
    assert codecs.utf_8_encode(u"\U00080000") == (b"\xf0\xa0\x80\x80", 4)
    assert codecs.utf_8_encode(u"\U0010ffff") == (b"\xf4\x8f\xbf\xbf", 4)
    assert codecs.
