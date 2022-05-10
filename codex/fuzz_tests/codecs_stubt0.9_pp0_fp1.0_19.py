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

class TestIncrementalDecoder(unittest.TestCase):
    def test_error_callbacks(self):
        self.assertRaises(codecs.LookupError,
                          codecs.lookup_error, "illegal_error_callback_name")
        self.assertRaises(TypeError, codecs.lookup_error, lambda x: 1)

        utf8 = codecs.getincrementaldecoder("utf-8")()
        utf8.set_error_handler(codecs.lookup_error("add_one_codepoint"))
        self.assertRaises(UnicodeDecodeError, utf8.decode, b'ab\xff\xff', False)
        self.assertEqual("a", utf8.decode(b'ab\xff\xff', True))
        self.assertEqual("a", utf8.decode(b'', True))

        utf8.set_error_handler(codecs.lookup_error("ignore"))
        self.assertEqual("", utf8.
