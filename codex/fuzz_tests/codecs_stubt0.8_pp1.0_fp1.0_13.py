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

def test_ascii_error_handler(test):
    test.test("test_ascii_error_handler", "abc", "abc")
    test.test("test_ascii_error_handler", "\xff", "\\xFF")
    test.test("test_ascii_error_handler", "\xff\x00", "\\xFF\\x00")
    test.test("test_ascii_error_handler", "\xff\x00\xff", "\\xFF\\x00\\xFF")
    test.test("test_ascii_error_handler", "\xff\x00\xff\x00", "\\xFF\\x00\\xFF\\x00")
    test.test("test_ascii_error_handler", "\xff\x00\xff\x00\xff", "\\xFF\\x00\\xFF\\x00\\xFF")
    test.test("test_ascii_error_handler", "\xff\x00\xff\x00\xff\x00", "\\xFF\\x00\\xFF
