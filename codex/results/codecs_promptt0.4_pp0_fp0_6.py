import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        # Test registering an error handler
        self.assertEqual(codecs.lookup_error('strict'),
                         (codecs.strict_errors, codecs.strict_errors))
        self.assertEqual(codecs.lookup_error('ignore'),
                         (codecs.ignore_errors, codecs.replace_errors))
        self.assertEqual(codecs.lookup_error('replace'),
                         (codecs.replace_errors, codecs.replace_errors))
        self.assertEqual(codecs.lookup_error('xmlcharrefreplace'),
                         (codecs.xmlcharrefreplace_errors,
                          codecs.xmlcharrefreplace_errors))
        self.assertEqual(codecs.lookup_error('backslashreplace'),
                         (codecs.backslashreplace_errors,
                          codecs.backslash
