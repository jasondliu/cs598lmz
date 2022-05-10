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
    def test_search_function(self):
        # search_function
        self.assertEqual(codecs.search_function('utf-8')(),
                         (None, None, None, None))

    def test_encode_decode(self):
        self.assertEqual(codecs.encode("abc"), (b"abc", 3))
        self.assertEqual(codecs.encode("abc", "rot13"), (b"nop", 3))
        self.assertEqual(codecs.encode("abc", "rot13", "strict"), (b"nop", 3))
        self.assertEqual(codecs.encode("abc", "rot13", "ignore"), (b"nop", 3))
        self.assertEqual(codecs.encode("abc", "rot13", "replace"), (b"?op", 3))
        self.assertEqual(codecs.encode("abc", "rot13", "xmlcharrefreplace"),

