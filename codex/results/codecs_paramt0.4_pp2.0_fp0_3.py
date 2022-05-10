import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):

    def test_encode_utf8(self):
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x9f', 'äöüß'.encode('utf-8'))
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x9f', 'äöüß'.encode('utf-8', 'strict'))
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x9f', 'äöüß'.encode('utf-8', 'replace'))
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x9f', 'äöüß'.encode('utf-8', 'ignore'))
        self.assertEqual(b'
