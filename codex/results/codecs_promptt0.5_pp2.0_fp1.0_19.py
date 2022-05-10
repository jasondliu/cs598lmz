import codecs
# Test codecs.register_error()
# This is needed to test the 'xmlcharrefreplace' error handler

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test 'xmlcharrefreplace' error handler
        self.assertEqual(codecs.xmlcharrefreplace_errors('test'), 'test')
        self.assertEqual(codecs.xmlcharrefreplace_errors(u'test'), u'test')
        self.assertEqual(codecs.xmlcharrefreplace_errors(u't\u00e9st'),
                         u't&#233;st')
        self.assertEqual(codecs.xmlcharrefreplace_errors(u't\u0153st'),
                         u't&#337;st')
        self.assertEqual(codecs.xmlcharrefreplace_errors(u't\ufffst'),
                         u't&#65533;st')
        self.assertEqual(codecs.xmlcharrefreplace_errors(u't\u0100st'),

