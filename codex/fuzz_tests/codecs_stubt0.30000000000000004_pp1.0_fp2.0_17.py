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

    def test_encode(self):
        self.assertEqual(codecs.encode("abc"), b"abc")
        self.assertEqual(codecs.encode("abc", "rot-13"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "strict"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "ignore"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "replace"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "backslashreplace"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "xmlcharrefreplace"), b"nop")
        self.assertEqual(codecs.encode("abc", "rot-13", "namereplace
