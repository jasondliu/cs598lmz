import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_encoding(unittest.TestCase):
    def test_encoding(self):
        """Test encoding of a string"""
        self.assertEqual(encoding("abc"), "abc")
        self.assertEqual(encoding("abc\x80"), "abc\uFFFD")
        self.assertEqual(encoding("abc\x80\x81"), "abc\uFFFD\uFFFD")
        self.assertEqual(encoding("abc\x80\x81\x82"), "abc\uFFFD\uFFFD\uFFFD")
        self.assertEqual(encoding("abc\x80\x81\x82\x83"), "abc\uFFFD\uFFFD\uFFFD\uFFFD")

    def test_encoding_utf8(self):
        """Test encoding of a utf-8 string"""
        self.assertEqual(encoding("abc\xe2\x80\x99"), "abc\u2019")
        self.assertEqual
