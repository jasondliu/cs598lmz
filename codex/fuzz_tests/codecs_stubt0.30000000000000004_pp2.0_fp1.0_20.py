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

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xff'), ('\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\x28'), ('\ufffd(', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xe2\x28\xa1'), ('\ufffd(?', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xe2\x82\x28'), ('\u2028', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xf0\x90\x8c\xbc'), ('\U0001D11E', 4))
        self.assertEqual(codecs
