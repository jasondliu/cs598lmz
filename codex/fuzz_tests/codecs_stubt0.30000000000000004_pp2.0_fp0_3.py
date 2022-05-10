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
    # Test UTF-16
    for encoding in ("utf-16-le", "utf-16-be"):
        for error_handler in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"):
            f = codecs.open(TESTFN, "w", encoding, errors=error_handler)
            f.write("\xff")
            f.close()
            f = codecs.open(TESTFN, "r", encoding, errors=error_handler)
            if error_handler == "strict":
                raises(UnicodeError, f.read)
            elif error_handler == "replace":
                assert f.read() == "\ufffd"
            elif error_handler == "ignore":
                assert f.read() == ""
            elif error_handler == "add_one_codepoint":
                assert f.read() == "a"
            elif error_handler == "add_utf16_bytes":
                assert f.read() == "\ufffd\
