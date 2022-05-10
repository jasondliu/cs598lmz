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

# Test that the codecs module is working properly

class CodecsModuleTest(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(codecs.encode("abc", "rot13"), "nop")
        self.assertEqual(codecs.encode("abc", "rot13", "strict"), "nop")
        self.assertEqual(codecs.encode("abc", "rot13", "ignore"), "nop")
        self.assertEqual(codecs.encode("abc", "rot13", "replace"), "nop?")
        self.assertEqual(codecs.encode("abc", "rot13", "backslashreplace"), "nop\\")
        self.assertEqual(codecs.encode("abc", "rot13", "xmlcharrefreplace"), "nop&#78;")
        self.assertEqual(codecs.encode("abc", "rot13", "add_one_codepoint"), "nopa")
        self.assertE
