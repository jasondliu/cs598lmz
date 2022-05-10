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
    # UTF-8
    assert codecs.decode("\x80", "utf-8", "strict") == "\uFFFD"
    assert codecs.decode("\x80", "utf-8", "replace") == "\uFFFD"
    assert codecs.decode("\x80", "utf-8", "ignore") == ""
    assert codecs.decode("\x80", "utf-8", "add_one_codepoint") == "a"
    assert codecs.decode("\x80", "utf-8", "add_utf16_bytes") == "\uFFFD"
    assert codecs.decode("\x80", "utf-8", "add_utf32_bytes") == "\uFFFD"
    assert codecs.decode("\x80", "utf-8", "backslashreplace") == "\\x80"
    assert codecs.decode("\x80", "utf-8", "xmlcharrefreplace") == "&#128;"

    # UTF-16
    assert
