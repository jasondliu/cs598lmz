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

class TestDecoding:

    def test_utf8(self):
        u = "a\u03a9"
        b = u.encode("utf-8")
        # with errors=strict, a truncated string raises an exception
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf-8", "strict")
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf-8", "replace", 1)
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf-8", "ignore", 1)
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf-8", "replace")
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf-8", "ignore")
        with self.assertRaises(UnicodeDecodeError):
            b[:-1].decode("utf
