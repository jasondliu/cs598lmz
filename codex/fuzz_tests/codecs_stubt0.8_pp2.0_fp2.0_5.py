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

def test_readline():
    # Test that readline works decently
    f = io.BytesIO(b"abc\nabc\nabc\n")
    r = codecs.getreader("utf-16")(f)
    assert r.readline() == "\u6261\u6261\u6261\n"
    assert r.readline() == "\u6261\u6261\u6261\n"
    assert r.readline() == "\u6261\u6261\u6261\n"
    assert r.readline() == ""

def test_utf16_error_handling():
    f = io.BytesIO(b"abc\nabc\nabc\n")
    r = codecs.getreader("utf-16")(f)
    assert r.readline() == "\u6261\u6261\u6261\n"
    # If we don't pass errors="add_one_codepoint", we get a UnicodeDecodeError
    # at the first character of the next line.
    try:

