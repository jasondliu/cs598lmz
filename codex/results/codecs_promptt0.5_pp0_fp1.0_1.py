import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        with self.assertRaises(ValueError):
            codecs.register_error('strict', codecs.strict_errors)
        with self.assertRaises(LookupError):
            codecs.register_error('ignore', codecs.ignore_errors)
        with self.assertRaises(LookupError):
            codecs.register_error('replace', codecs.replace_errors)
        with self.assertRaises(LookupError):
            codecs.register_error('xmlcharrefreplace',
                                  codecs.xmlcharrefreplace_errors)
        with self.assertRaises(LookupError):
            codecs.register_error('backslashreplace',
                                  codecs.backslashreplace_errors)


class Test_lookup_error(unittest.TestCase):
    def test_lookup_error(self):
        self.assertEqual(codecs.lookup
