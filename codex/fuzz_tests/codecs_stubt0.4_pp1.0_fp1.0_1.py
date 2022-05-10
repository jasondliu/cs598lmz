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
    # Test UTF-8 encoding
    assert codecs.utf_8_encode("abc") == (b'abc', 3)
    assert codecs.utf_8_encode("ab\u20ac") == (b'ab\xe2\x82\xac', 5)
    assert codecs.utf_8_encode("\U0001D11E") == (b'\xf0\x9d\x84\x9e', 4)

    # Test UTF-8 decoding
    assert codecs.utf_8_decode(b'abc') == ('abc', 3)
    assert codecs.utf_8_decode(b'ab\xe2\x82\xac') == ('ab\u20ac', 5)
    assert codecs.utf_8_decode(b'\xf0\x9d\x84\x9e') == ('\U0001D11E', 4)

    # Test UTF-8 decoding with errors
    assert codecs.utf_8_decode(b'ab\xff') == ('ab
