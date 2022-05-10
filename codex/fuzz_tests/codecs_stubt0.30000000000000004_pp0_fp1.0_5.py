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
    # test UTF-8
    for encoding in ("utf-8", "utf_8"):
        assert codecs.decode("\x80", encoding) == "\uFFFD"
        assert codecs.decode("\x80", encoding, "replace") == "\uFFFD"
        assert codecs.decode("\x80", encoding, "ignore") == ""
        assert codecs.decode("\x80", encoding, "add_one_codepoint") == "a"
        assert codecs.decode("\x80", encoding, "add_utf16_bytes") == "\uFFFD"
        assert codecs.decode("\x80", encoding, "add_utf32_bytes") == "\uFFFD"
        assert codecs.decode("\x80", encoding, "surrogateescape") == "\udc80"
        assert codecs.decode("\x80", encoding, "surrogatepass") == "\udc80"
        assert codecs.decode("\x80", encoding, "xmlcharrefreplace
