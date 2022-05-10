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

class TestUTF8(unittest.TestCase):

    def test_utf8_decode_error(self):
        self.assertEqual(b'\x80'.decode("utf-8", "strict"), u'\uFFFD')
        self.assertEqual(b'\x80'.decode("utf-8", "ignore"), u'')
        self.assertEqual(b'\x80'.decode("utf-8", "replace"), u'\uFFFD')
        self.assertEqual(b'\x80'.decode("utf-8", "backslashreplace"), u'\\x80')
        self.assertEqual(b'\x80'.decode("utf-8", "xmlcharrefreplace"), u'&#128;')
        self.assertEqual(b'\x80'.decode("utf-8", "namereplace"), u'\\x80')
        self.assertEqual(b'\x80'.decode("utf-8", "add_one_codepoint"), u'a\uFFFD')
