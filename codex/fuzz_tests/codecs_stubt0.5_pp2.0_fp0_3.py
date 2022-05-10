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
    data = b'\xff'
    assert data.decode("utf-8", "add_one_codepoint") == "a\ufffd"
    assert data.decode("utf-16", "add_one_codepoint") == "\ufffd"
    assert data.decode("utf-32", "add_one_codepoint") == "\ufffd"
    assert data.decode("ascii", "add_one_codepoint") == "\ufffd"
    assert data.decode("latin-1", "add_one_codepoint") == "\ufffd"

def test_add_utf16_bytes():
    data = b'\xff'
    assert data.decode("utf-8", "add_utf16_bytes") == "\ufffd"
    assert data.decode("utf-16", "add_utf16_bytes") == "\ufffd"
    assert data.decode("utf-32", "add_utf16_bytes") == "\ufffd"
    assert data
