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

def create_test(name, bytes, decoder, expected):
    def test(self):
        self.assertEqual(
            codecs.decode(bytes, decoder),
            expected,
        )
    test.__name__ = name
    return test

class ErrorHandlingTest(unittest.TestCase):
    def test_decode_errors(self):
        for errors, decoder, y in (
            ("strict", "utf-8", ValueError),
            ("strict", "utf-16", ValueError),
            ("strict", "utf-32", ValueError),
            ("ignore", "utf-8", b""),
            ("ignore", "utf-16", b""),
            ("ignore", "utf-32", b""),
            ("replace", "utf-8", b"?"),
            ("replace", "utf-16", b"\xff\xfd"),
            ("replace", "utf-32", b"\xff\xff\xff\xfd"),
            ("add_one_codepoint", "utf-8", b"
