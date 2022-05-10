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

# Test that the codecs module is working

def test_codecs():
    # Test the UTF-8 codec
    assert codecs.utf_8_encode(u"abc") == (b"abc", 3)
    assert codecs.utf_8_encode(u"abc\u1234") == (b"abc\xe1\x88\xb4", 7)
    assert codecs.utf_8_decode(b"abc") == (u"abc", 3)
    assert codecs.utf_8_decode(b"abc\xe1\x88\xb4") == (u"abc\u1234", 7)
    assert codecs.utf_8_decode(b"abc\xe1\x88\xb4", "replace") == (u"abc\ufffd", 7)
    assert codecs.utf_8_decode(b"abc\xe1\x88\xb4", "ignore") == (u"abc", 7)
    assert codecs.utf_8_decode(b"abc\xe1\x88\
