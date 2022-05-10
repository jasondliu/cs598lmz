import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

class Test_codecs(unittest.TestCase):

    def test_utf8_error(self):
        self.assertEqual(codecs.utf_8_decode("abc\xff", "strict", True), ("abc\xff", 5))
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, "abc\xff", "strict", False)
        self.assertEqual(codecs.utf_8_decode("abc\xff", "ignore", False), ("abc", 5))
        self.assertEqual(codecs.utf_8_decode("abc\xff\u1234", "replace", False), ("abc\ufffd\u1234", 7))
        #self.assertRaises(TypeError, codecs.utf_8_decode, "abc\xff", 42)
        self.assertRaises(TypeError, codecs.utf_8_decode, "abc\xff", "strict", 42)
