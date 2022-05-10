import codecs
# Test codecs.register_error()

import codecs
import test.test_support

from test import test_support

class CodecRegErrorTest(unittest.TestCase):
    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(TypeError, codecs.register_error, 'strict', 42)
        self.assertRaises(LookupError, codecs.register_error, '__builtin__')
        self.assertRaises(LookupError, codecs.register_error, '__builtin__',
                          'strict')
        self.assertRaises(LookupError, codecs.register_error, '__builtin__',
                          'ignore')
        self.assertRaises(LookupError, codecs.register_error, '__builtin__',
                          'replace')
        self.assertRaises(LookupError, codecs.register_error, '__builtin__',
                          'xmlcharrefreplace')
        self.assertRaises(LookupError
