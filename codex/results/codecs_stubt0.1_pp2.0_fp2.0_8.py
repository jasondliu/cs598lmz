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

class Test_UTF16(unittest.TestCase):
    def test_utf16_decode(self):
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', 'strict', True),
                         ('abc', 6))
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfe\x00\x61\x00\x62\x00\x63', 'strict', False),
                         ('abc', 6))
        self.assertEqual(codecs.utf_16_decode(b'\x00\x61\x00\x62\x00\x63', 'strict', True),
                         ('abc', 6))
        self.assertEqual(codecs.utf_16_decode(b'\x00\x61\x00\x62\x00\x63', 'strict', False),
                         ('abc', 6))
        self.assert
