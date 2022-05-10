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

class TestUnicodeErrors:

    def test_decode(self):
        from collections import namedtuple
        from _testcapi import make_surrogate
        TestPoint = namedtuple("TestPoint", "name testdata expected input_bytes")
        testpoints = (
            ("backslashreplace", b"abc\\xFFdef", "abc\ufffddef", True),
            ("ignore", b"abc\\xFFdef", "abcdef", True),
            ("replace", b"abc\\xFFdef", "abc\ufffddef", True),
            ("xmlcharrefreplace", b"abc\\xFFdef", "abc&#255;def", True),
            ("backslashreplace", b"\uFFFE", "\\uFFFE", False),
            ("ignore", b"\uFFFE", "", False),
            ("replace", b"\uFFFE", "\ufffd", False),
            ("xmlcharrefreplace", b"\uFFFE", "\ufffd", False),
            ("backslashreplace", b"a\\xFFb",
