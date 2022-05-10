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

class UTF16Test(unittest.TestCase):
    def test_utf16_decode(self):
        self.assertEqual(unicode(b"\xff\xfex\x00", "utf-16-be"), u"x")
        self.assertEqual(unicode(b"x\x00\xff\xfe", "utf-16-le"), u"x")
        self.assertRaises(UnicodeError, unicode, b"x\x00", "utf-16-be")
        self.assertRaises(UnicodeError, unicode, b"\x00x", "utf-16-le")
        self.assertRaises(UnicodeError, unicode, b"\xff\xfe", "utf-16-le")
        self.assertRaises(UnicodeError, unicode, b"\xff\xfe", "utf-16-be")
        self.assertRaises(UnicodeError, unicode, b"\xff\xff", "utf-16-le")
        self.assertRaises(Un
