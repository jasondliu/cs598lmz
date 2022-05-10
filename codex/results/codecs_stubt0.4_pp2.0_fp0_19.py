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

class Test_utf_16_be_codec(unittest.TestCase):
    def test_utf_16_be_encode(self):
        self.assertEqual(
            codecs.utf_16_be_encode("abc"),
            (b"\x00a\x00b\x00c", 3)
        )
        self.assertEqual(
            codecs.utf_16_be_encode("abc", "strict"),
            (b"\x00a\x00b\x00c", 3)
        )
        self.assertEqual(
            codecs.utf_16_be_encode("abc\uDC80"),
            (b"\x00a\x00b\x00c\xDC\x80", 5)
        )
        self.assertEqual(
            codecs.utf_16_be_encode("abc\uDC80", "strict"),
            (b"\x00a\x00b\x00c\xDC\x80", 5)
        )
       
