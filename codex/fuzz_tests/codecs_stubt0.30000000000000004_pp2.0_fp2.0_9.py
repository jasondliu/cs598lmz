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
    assert codecs.decode("\xff", "utf-8", "strict") == "\ufffd"
    assert codecs.decode("\xff", "utf-8", "ignore") == ""
    assert codecs.decode("\xff", "utf-8", "replace") == "\ufffd"
    assert codecs.decode("\xff", "utf-8", "add_one_codepoint") == "a"
    assert codecs.decode("\xff", "utf-8", "add_utf16_bytes") == "ab"
    assert codecs.decode("\xff", "utf-8", "add_utf32_bytes") == "abcd"

    # UTF-16
    assert codecs.decode(b"\xff", "utf-16", "strict") == "\ufffd"
    assert codecs.decode(b"\xff", "utf-16", "ignore") == ""
    assert codecs.decode(b"\xff", "utf-16", "replace")
