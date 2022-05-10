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

class TestDecode(unittest.TestCase):

    def test_utf8_decode(self):
        for i in range(0, 0xd7ff):
            self.assertEqual(chr(i).encode("utf-8").decode("utf-8"), chr(i))
        for i in range(0xe000, 0x10ffff):
            self.assertEqual(chr(i).encode("utf-8").decode("utf-8"), chr(i))
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b"\xff\xff".decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b"\xff\xff\xff".decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b"\xff\xff\xff\xff".decode, "utf-8")
        self.assertRaises(Unic
