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

class TestErrorHandlers(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual("a".encode("iso-8859-1", "replace"),
                         str("a".encode("iso-8859-1", "add_one_codepoint")))

        self.assertEqual("a".encode("iso-8859-1", "replace"),
                         str("".encode("iso-8859-1", "add_one_codepoint")))

        self.assertEqual("abc".encode("iso-8859-1", "replace"),
                         str("abc".encode("iso-8859-1", "add_one_codepoint")))

    def test_add_utf16_bytes(self):
        self.assertEqual(b'ab', b'a'.encode('utf-16', 'add_utf16_bytes'))

    def test_add_utf32_bytes(self):
        self.assertEqual(b'abcd', b'a'.encode
