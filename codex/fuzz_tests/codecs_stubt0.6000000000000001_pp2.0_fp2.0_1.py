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

class TestUtf16(unittest.TestCase):
    def test_decode(self):
        # UCS-2
        self.assertEqual("\xe9\u20ac".encode("utf-16"), b'\x00\xe9\x20\xac')
        # UCS-4
        self.assertEqual("\U00012345".encode("utf-16"), b'\x00\x01\x23\x45')
        self.assertEqual(b'\xff\xfe\x00\xe9\x20\xac'.decode("utf-16"),
                         "\xe9\u20ac")
        self.assertEqual(b'\xfe\xff\x00\xe9\x20\xac'.decode("utf-16"),
                         "\xe9\u20ac")

    def test_encode(self):
        # UCS-2
        self.assertEqual("\xe9\u20ac".encode("utf-16"), b'\x00\xe9\x20\xac')
