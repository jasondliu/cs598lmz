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

class TestDecodeErrorHandling(unittest.TestCase):
    class TestErrorHandler(unittest.TestCase):
        def test_decoding(self):
            for encoding in ALL_UTF_ENCODINGS:
                for handler in (None, "strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
                    try:
                        codecs.decode(b"\xff", encoding, handler)
                    except UnicodeDecodeError as exc:
                        self.assertEqual(exc.encoding, encoding)
                        self.assertEqual(exc.object, b"\xff")
                        self.assertEqual(exc.start, 0)
                        self.assertEqual(exc.end, 1)
                        if handler == "add_one_codepoint":
                            self.assertEqual(exc.reason, "add_one_codepoint")
                        elif handler == "add_utf16_bytes":
                            self.assertEqual(exc.reason, "add_
