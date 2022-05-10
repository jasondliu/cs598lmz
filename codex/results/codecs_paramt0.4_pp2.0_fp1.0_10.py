import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_unicode(unittest.TestCase):

    def test_unicode(self):
        self.assertEqual(unicode(u'abc'), 'abc')
        self.assertEqual(unicode(u'\xe9'), '\xe9')
        self.assertEqual(unicode(u'\u20ac'), '\u20ac')
        self.assertEqual(unicode(u'\U0001d120'), '\U0001d120')

    def test_unicode_with_encoding(self):
        self.assertEqual(unicode(u'\xe9', 'latin-1'), '\xe9')
        self.assertEqual(unicode(u'\xe9', 'utf-8'), '\xe9')
        self.assertEqual(unicode(u'\u20ac', 'utf-8'), '\u20ac')
        self.assertEqual(unicode(u'\U0001d120', 'utf-8'), '\U0001d120')
