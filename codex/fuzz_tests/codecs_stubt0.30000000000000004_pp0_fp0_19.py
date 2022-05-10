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
    # test utf-16-le
    for errors in ("strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes"):
        s = b'\xff\xfe\x00\x00\x00\x00\x00\x00'
        if errors == "add_one_codepoint":
            s = b'\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00'
        elif errors == "add_utf16_bytes":
            s = b'\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        try:
            s.decode("utf-16-le", errors)
        except UnicodeDecodeError:
            pass
        else:
            raise AssertionError("should have raised UnicodeDecodeError")

    # test utf-16-be
    for errors in ("strict",
