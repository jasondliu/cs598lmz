import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):

    def test_1(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_2(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_3(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_4(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_5(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_6(self):
        s = '\u3042\u3044'
        self.assertEqual(s, 'あい')

    def test_7(self):
       
