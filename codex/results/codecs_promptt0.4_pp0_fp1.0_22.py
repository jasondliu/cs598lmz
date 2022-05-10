import codecs
# Test codecs.register_error('test', codecs.ignore_errors)
# Test codecs.register_error('test', codecs.replace_errors)
# Test codecs.register_error('test', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('test', codecs.backslashreplace_errors)
# Test codecs.register_error('test', codecs.namereplace_errors)

# Test codecs.lookup_error('test')

# Test UnicodeEncodeError
class TestUnicodeEncodeError(unittest.TestCase):

    def test_init(self):
        # calling UnicodeEncodeError with a string
        self.assertRaises(TypeError, codecs.UnicodeEncodeError, "abc")
        # calling UnicodeEncodeError with a wrong number of parameters
        self.assertRaises(TypeError, codecs.UnicodeEncodeError)
        self.assertRaises(TypeError, codecs.UnicodeEncodeError, "abc", 1, 2, 3)
        # calling UnicodeEncodeError with an invalid end
       
