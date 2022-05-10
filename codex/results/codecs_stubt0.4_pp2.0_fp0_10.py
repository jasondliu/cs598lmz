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

    def test_decode(self):
        self.assertEqual(codecs.decode("abc", "ascii"), "abc")
        self.assertEqual(codecs.decode(b"abc", "ascii"), "abc")
        self.assertEqual(codecs.decode(bytearray(b"abc"), "ascii"), "abc")
        self.assertEqual(codecs.decode(memoryview(b"abc"), "ascii"), "abc")
        self.assertEqual(codecs.decode("äöü", "latin-1"), "äöü")
        self.assertEqual(codecs.decode(b"\xe4\xf6\xfc", "latin-1"), "äöü")
        self.assertEqual(codecs.decode(bytearray(b"\xe4\xf6\xfc"), "latin-1"), "äöü")
        self.assertE
