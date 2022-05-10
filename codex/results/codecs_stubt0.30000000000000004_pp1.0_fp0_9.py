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

def test_add_one_codepoint():
    # Test that adding one codepoint at the start of the string works
    # correctly.
    #
    # This is a regression test for issue #12095.
    s = b'\xed\xa0\x80' # U+D800
    s = s.decode('utf-16-le', 'add_one_codepoint')
    assert s == 'a\ud800'

def test_add_utf16_bytes():
    # Test that adding two UTF-16 bytes at the start of the string
    # works correctly.
    #
    # This is a regression test for issue #12095.
    s = b'\xed\xa0\x80' # U+D800
    s = s.decode('utf-16-le', 'add_utf16_bytes')
    assert s == 'ab\ud800'

def test_add_utf32_bytes():
    # Test that adding four UTF-32 bytes at the start of the string
    # works correctly.
    #
