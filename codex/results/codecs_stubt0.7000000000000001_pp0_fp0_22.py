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

class TestUTF8(unittest.TestCase):
    def test_incomplete(self):
        # This test is validating that we don't crash.
        # see bug #117794
        self.assertRaises(UnicodeDecodeError, unicode, "\x80", "utf8",
                          "replace")

    def test_decode_error_handling(self):
        # Issue #15201 - return correct endianness of original byte input when
        # error handler is called
        for (encoding, input, errors, expected_output) in (
            ("utf-8", b'\xff', "add_one_codepoint", "\xc3\xbf"),
            ("utf-16-le", b'\xff\xfe', "add_utf16_bytes", "\xff\xfe\x00a\x00"),
            ("utf-16-be", b'\xff\xfe', "add_utf16_bytes", "\x00\xff\x00a"),
            ("utf-32-le", b'\xff\xfe', "
