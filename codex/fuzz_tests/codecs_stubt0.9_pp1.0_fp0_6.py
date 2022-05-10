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

class UnicodeTranslateErrorTest(unittest.TestCase):

    def test_init(self):
        e = UnicodeTranslateError('x', u'y', 1, 2, 'z')
        self.assertEqual(str(e), "can't translate character u'x' in position 1: z")
        self.assertEqual(e.encoding, 'y')
        self.assertEqual(e.object, u'y')
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 2)
        self.assertEqual(e.reason, 'z')

    def test_unicode(self):
        e = UnicodeTranslateError('x', u'y', 1, 2, 'z')
        self.assertEqual(unicode(e), u"can't translate character u'x' in position 1: z")
        self.assertEqual(e.encoding, 'y')
        self.assertEqual(e.object, u'y')
        self.assertEqual(e.start, 1
