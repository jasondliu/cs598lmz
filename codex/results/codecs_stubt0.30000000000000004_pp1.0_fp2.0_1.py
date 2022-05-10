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

# Test the error handlers

def test_error_handlers():
    # test the add_one_codepoint error handler
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "latin-1", "add_one_codepoint") == "a\x80"
    assert codecs.decode("\x80", "
