import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

# Test codecs.lookup_error('strict')
# Test codecs.lookup_error('ignore')
# Test codecs.lookup_error('replace')
# Test codecs.lookup_error('xmlcharrefreplace')
# Test codecs.lookup_error('backslashreplace')

class TestIncrementalEncoder(unittest.TestCase):

    def test_lone_surrogates(self):
        # lone surrogates should be detected in incremental encoder
        encoder = codecs.getincrementalencoder('utf-16-le')('strict')
        self.assertRaises(UnicodeEncodeError
