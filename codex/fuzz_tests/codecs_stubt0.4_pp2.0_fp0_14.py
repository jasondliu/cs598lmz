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

class CodecsModuleTest(unittest.TestCase):
    def test_encode_decode(self):
        # test codecs.encode() and codecs.decode()
        self.assertEqual(codecs.encode("abc"), b"abc")
        self.assertEqual(codecs.encode(b"abc"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii"), b"abc")
        self.assertEqual(codecs.encode(b"abc", "ascii"), b"abc")
        self.assertEqual(codecs.decode(b"abc"), "abc")
        self.assertEqual(codecs.decode("abc"), "abc")
        self.assertEqual(codecs.decode(b"abc", "ascii"), "abc")
        self.assertEqual(codecs.decode("abc", "ascii"), "abc")
        self.assertRaises(TypeError, codecs.encode)

