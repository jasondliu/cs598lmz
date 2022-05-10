import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8(self):
        f = codecs.open('test.txt', 'r', 'utf-8')
        self.assertEqual(f.read(), '\u20ac')

    def test_utf8_strict(self):
        f = codecs.open('test.txt', 'r', 'utf-8', 'strict')
        self.assertEqual(f.read(), '\u20ac')

    def test_latin1(self):
        f = codecs.open('test.txt', 'r', 'latin-1')
        self.assertEqual(f.read(), '\u20ac')

    def test_latin1_strict(self):
        f = codecs.open('test.txt', 'r', 'latin-1', 'strict')
        self.assertEqual(f.read(), '\u20ac')

    def test_ascii(self):
        f = codecs.open
