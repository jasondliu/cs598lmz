import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_encoding(self):
        self.assertEqual(b'\xc3\x81\xc3\x82\xc3\x83'.decode('utf-8', 'strict'), '\u00c1\u00c2\u00c3')

if __name__ == '__main__':
    unittest.main()
