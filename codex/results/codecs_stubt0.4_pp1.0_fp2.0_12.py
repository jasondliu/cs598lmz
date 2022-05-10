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
    # Test the add_one_codepoint error handler
    assert codecs.decode("abc", "ascii", "add_one_codepoint") == "aabc"
    assert codecs.decode("abc\xff", "ascii", "add_one_codepoint") == "aabc\xff"
    assert codecs.decode("abc\xff", "ascii", "add_one_codepoint") == "aabc\xff"
    assert codecs.decode("\xff", "ascii", "add_one_codepoint") == "\xff"
    assert codecs.decode("\xff", "ascii", "add_one_codepoint") == "\xff"
    raises(UnicodeDecodeError, codecs.decode, "\xff\xff", "ascii", "add_one_codepoint")
    raises(UnicodeDecodeError, codecs.decode, "\xff\xff", "ascii", "add_one_codep
