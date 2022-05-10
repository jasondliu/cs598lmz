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
    # Try UTF-8
    test_utf8()
    # Try UTF-16
    test_utf16()
    # Try UTF-32
    test_utf32()

def test_utf8():
    # Check that UnicodeEncodeError is raised correctly on encoding errors
    for i in range(0, 0xd800):
        s = chr(i)
        check_encode(s, "utf-8", "strict")
        check_encode(s, "utf-8", "ignore")
        check_encode(s, "utf-8", "replace")
        check_encode(s, "utf-8", "backslashreplace")
        check_encode(s, "utf-8", "xmlcharrefreplace")
        check_encode(s, "utf-8", "add_one_codepoint")
        check_encode(s, "utf-8", "surrogateescape")
        check_encode(s, "utf-8", "surrogatepass")

    # Check that Unicode
