import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):

    def test_utf8(self):
        f = codecs.open('test_utf8.txt', 'r', 'utf-8')
        try:
            s = f.read()
        finally:
            f.close()
        self.assertEqual(s, u'\u20ac\n')

    def test_utf8_bom(self):
        f = codecs.open('test_utf8_bom.txt', 'r', 'utf-8-sig')
        try:
            s = f.read()
        finally:
            f.close()
        self.assertEqual(s, u'\u20ac\n')

    def test_utf8_bom_strict(self):
        f = codecs.open('test_utf8_bom.txt', 'r', 'utf-8')
        try:
            s = f.read()
        finally:
            f.close()
        self.assertEqual(s
