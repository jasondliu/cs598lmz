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

class TestUnicodeDecode(unittest.TestCase):
    def test_decode(self):
        self.assertEqual("abc", "ab".decode("ascii", "add_one_codepoint"))
        self.assertEqual("abc", "ab".decode("utf-16", "add_utf16_bytes"))
        self.assertEqual("abc", "ab".decode("utf-32", "add_utf32_bytes"))

class TestUnicodeEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(b"abc", "ab".encode("ascii", "add_one_codepoint"))
        self.assertEqual(b"abc", "ab".encode("utf-16", "add_utf16_bytes"))
        self.assertEqual(b"abc", "ab".encode("utf-32", "add_utf32_bytes"))

class TestOpen(unittest.TestCase):
    def test_io_open(self):

