import codecs
# Test codecs.register_error for error handling
# Test codecs.lookup_error for error handling
# Test codecs.strict_errors for error handling
# Test codecs.ignore_errors for error handling
# Test codecs.replace_errors for error handling
# Test codecs.xmlcharrefreplace_errors for error handling
# Test codecs.backslashreplace_errors for error handling
# Test codecs.namereplace_errors for error handling
class TestFunctions(unittest.TestCase):
    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, 'replace', 'foo')
        self.assertRaises(TypeError, codecs.register_error, 'foo', lambda x: x)
        self.assertRaises(LookupError, codecs.register_error, 'foo', lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, 'xmlcharrefreplace', lambda x, y: x)

    def test_lookup_error(self):
        self.assertRaises(LookupError, codecs.
