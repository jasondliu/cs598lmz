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
    text = "spam\n"
    text_encode = b"spam\n"
    text_decode = "spam\n"

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint",
                          lambda x: (u"a", x.start))
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint",
                          lambda x: (b"a", x.start))
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint",
                          lambda x: (1, x.start))
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint",
                          lambda x: (u"a", x.start, x.end))
        self.assertRaises(TypeError, codecs.register_error, "add_one_cod
