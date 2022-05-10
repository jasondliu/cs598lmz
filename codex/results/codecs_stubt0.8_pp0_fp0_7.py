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

def check_error_handler(testfn, encoding, expected_error_name, expected_b, expected_s):
    try:
        testfn(encoding)
    except UnicodeError as e:
        if name != e.__class__.__name__:
            print(e.__class__.__name__, e.reason, e.encoding, e.object)
            raise
        b, s = codecs.lookup_error(expected_error_name)(e)
        assert b == expected_b, (b, expected_b)
        assert s == expected_s, (s, expected_s)
    else:
        raise AssertionError("Expected exception not raised")

def test_utf16(encoding, byteorder):
    def convert(encoding):
        codecs.decode("a\uffff", encoding)
    check_error_handler(convert, encoding, "add_one_codepoint", b"a", 1)

def test_utf16_be():
    test_utf16("utf-16-be", "big
