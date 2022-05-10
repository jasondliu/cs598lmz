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

class ErrorHandlingTest(unittest.TestCase):
    def testBasics(self):
        f = codecs.getreader("utf-16-le")("abcd")
        self.assertEquals("", f.read())
        self.assertEquals("a\ufeff", f.read())
        self.assertEquals("d", f.readline())

        f = codecs.getreader("utf-16-le")("")
        self.assertRaises(UnicodeDecodeError, f.readline)

        f = codecs.getreader("utf-16-le")("\0a\0e")
        self.assertEquals(u"a\ue000", f.read())
        self.assertEquals(u"b", f.read())

        f = codecs.getreader("utf-16-be")("\0a\0e")
        self.assertEquals(u"a\ue000", f.read())
        self.assertEquals(u"b", f.read())

        f = codecs.getreader("
