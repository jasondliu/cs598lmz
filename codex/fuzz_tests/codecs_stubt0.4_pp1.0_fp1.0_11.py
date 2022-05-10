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
    if sys.maxunicode == 0xffff:
        utf16_error_handler = "add_utf16_bytes"
    else:
        utf16_error_handler = "add_one_codepoint"
    utf32_error_handler = "add_utf32_bytes"

    # Test UTF-16-LE and UTF-16-BE
    for encoding in ("utf-16-le", "utf-16-be"):
        # Test decoding
        assert codecs.decode(b"\xff\xfe", encoding, "replace") == "\ufffd"
        assert codecs.decode(b"\xff\xfe", encoding, "ignore") == ""
        assert codecs.decode(b"\xff\xfe", encoding, "backslashreplace") == "\\ufffd"
        assert codecs.decode(b"\xff\xfe", encoding, "xmlcharrefreplace") == "&#65533;"
        assert codecs.decode(b"\xff\xfe", encoding, utf16
