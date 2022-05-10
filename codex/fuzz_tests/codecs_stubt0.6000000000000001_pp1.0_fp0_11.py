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

def test_utf8_error_handling():
    assert codecs.decode(b'\xe1', "utf-8", "strict") == "\u00e1"
    assert codecs.decode(b'\xe1', "utf-8", "replace") == "\ufffd"
    raises(UnicodeDecodeError, codecs.decode, b'\xe1', "utf-8")
    raises(UnicodeDecodeError, codecs.decode, b'\xe1', "utf-8", "ignore")
    raises(UnicodeDecodeError, codecs.decode, b'\xe1', "utf-8", "backslashreplace")
    assert codecs.decode(b'\xe1', "utf-8", "add_one_codepoint") == "a\u00e1"
    assert codecs.decode(b'\xe1', "utf-8", "add_utf16_bytes") == "\ufffd\u00e1"
    assert codecs.decode(b'\xe1
