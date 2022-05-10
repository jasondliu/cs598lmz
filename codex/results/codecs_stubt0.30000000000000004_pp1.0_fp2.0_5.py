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
    # Make sure that the codecs module is always available.
    import codecs

    # Test the UTF-8 codec
    s = '\xe9\u20ac'
    assert codecs.utf_8_decode(b'\xe9\xe2\x82\xac', 'strict', True) == (s, 4)
    assert codecs.utf_8_decode(b'\xe9\xe2\x82', 'strict', True) == (s, 3)
    assert codecs.utf_8_decode(b'\xe9\xe2', 'strict', True) == (s, 2)
    assert codecs.utf_8_decode(b'\xe9', 'strict', True) == ('\xe9', 1)
    assert codecs.utf_8_decode(b'\xe9\xe2\x82', 'strict', False) == (s, 3)
    assert codecs.utf_8_decode(b'\xe9\xe2', 'strict',
