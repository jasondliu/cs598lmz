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

class TestCodecs(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual(u"\u0430".encode("utf-8"), b"\xd0\xb0")
        self.assertEqual(u"\u0430\u0441".encode("utf-8"), b"\xd0\xb0\xd1\x81")
        self.assertEqual(u"\u0430\u0441\u0432".encode("utf-8"), b"\xd0\xb0\xd1\x81\xd0\xb2")
        self.assertEqual(u"\u0430\u0441\u0432\u0433".encode("utf-8"), b"\xd0\xb0\xd1\x81\xd0\xb2\xd0\xb3")
        self.assertEqual(u"\u0430\u0441\u0432\u0433\u0434".encode("utf-8"), b"\xd0
