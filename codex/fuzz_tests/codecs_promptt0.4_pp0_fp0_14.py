import codecs
# Test codecs.register_error
#
# This is a test for the codecs module.

import codecs
import unittest

class CodecsRegisterErrorTest(unittest.TestCase):

    def test_register_error(self):
        # This tests the 'xmlcharrefreplace' error handler
        codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
        self.assertEqual(codecs.strict_errors('test.xmlcharrefreplace'),
                         codecs.xmlcharrefreplace_errors)
        self.assertEqual(codecs.lookup_error('test.xmlcharrefreplace'),
                         codecs.xmlcharrefreplace_errors)
        self.assertEqual(codecs.strict_errors('test.xmlcharrefreplace'),
                         codecs.lookup_error('test.xmlcharrefreplace'))
        self.assertEqual(codecs.xmlcharrefreplace_errors('test.xmlcharrefreplace'),
                         codecs.lookup_error('test.xmlcharrefreplace'))
        self.assertE
