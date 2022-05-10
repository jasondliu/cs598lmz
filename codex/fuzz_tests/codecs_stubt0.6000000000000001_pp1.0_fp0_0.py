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

class CodecTest(unittest.TestCase):

    def test_surrogates(self):
        # bug 887606
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16-le")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16-be")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16-ex")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16-le-ex")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-16-be-ex")
        self.assertRaises(UnicodeError, '\udc80'.encode, "utf-32")
        self.assertRaises(UnicodeError, '\udc80'.encode
