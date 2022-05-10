import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # testing unicode error handler
        ue = codecs.lookup_error('ignore')
        self.assertEqual(ue('abc', u'\u1234'), (u'abc', 3))
        self.assertEqual(ue('abc', u'\u1234\u5678'), (u'abc', 6))
        self.assertEqual(ue('abc', u'\u1234\u5678\u9abc'), (u'abc', 9))
        # testing byte error handler
        be = codecs.lookup_error('ignore')
        self.assertEqual(be('abc', '\x80'), ('abc', 1))
        self.assertEqual(be('abc', '\x80\x81'), ('abc', 2))
        self.assertEqual(be('abc', '\x80\x81\x82'), ('abc', 3))
        # testing unicode-escape byte error
