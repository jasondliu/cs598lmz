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

def test_error_handlers():
    # Check that the error handlers are called at the right time
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("abc\x80def", "ascii", "add_one_codepoint") == "abc\x80def"
    assert codecs.decode("
