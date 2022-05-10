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

class Test_unicode(unittest.TestCase):
    def test_constructor1(self):
        self.assertRaises(TypeError, unicode)
        self.assertRaises(TypeError, unicode, b'abc', 'utf-8', 'strict', 1)
        self.assertRaises(TypeError, unicode, b'abc', 'utf-8', 'strict', 1, 2)
        self.assertRaises(TypeError, unicode, b'abc', 'utf-8', 'strict', 1, 2, 3, 4)
        self.assertRaises(TypeError, unicode, b'abc', 'utf-8', 'strict', 1, 2, 3, 4, 5)

    def test_constructor2(self):
        self.assertEqual(unicode(''), u'')
        self.assertEqual(unicode(b'abc'), u'abc')
        self.assertEqual(unicode(b'abc', 'utf-8'), u'abc')
        self.assertEqual(unicode(b'
