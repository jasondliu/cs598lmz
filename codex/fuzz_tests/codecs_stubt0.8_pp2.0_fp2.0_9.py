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

def raise_unicode_exception(exc):
    raise exc

codecs.register_error("raise", raise_unicode_exception)

class TestUnicode(unittest.TestCase):
    def test_printing(self):
        self.assertEqual(repr(u'\u1234'), "'\u1234'")
        self.assertEqual(repr(u'\u1234'*10), "'\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234'")

        self.assertEqual(str(u'x'), 'x')
        self.assertEqual(str(u'x'*10), 'xxxxxxxxxx')

        self.assertEqual(u'\u1234'.encode('ascii', 'xmlcharrefreplace'), b'&#4660;')
        self.assertEqual(u'\u1234'.encode('ascii', 'ignore'), b'')
       
