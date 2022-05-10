import codecs
# Test codecs.register_error
import codecs
import unittest

class CodecsTest(unittest.TestCase):
    def test_register_error(self):
        # Testing the codecs.register_error() API
        def bad_decode(input, errors='strict'):
            return (u'', len(input))
        codecs.register_error('test.notanencoding', bad_decode)
        self.assertRaises(UnicodeDecodeError,
                          unicode, 'a string', 'test.notanencoding')
        self.assertRaises(LookupError,
                          unicode, 'a string', 'test.notanencoding', 'replace')
        self.assertRaises(LookupError,
                          unicode, 'a string', 'test.notanencoding', 'ignore')
        self.assertRaises(LookupError,
                          unicode, 'a string', 'test.notanencoding', 'xmlcharrefreplace')
