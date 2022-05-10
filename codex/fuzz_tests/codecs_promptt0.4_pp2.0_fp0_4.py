import codecs
# Test codecs.register_error('ignore')
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
#
# Test program for codecs.register_error()
#

import unittest
import codecs
import string

class CodecsTest(unittest.TestCase):

    def test_register_error(self):

        # Test the ignore error handler
        self.assertEqual(codecs.register_error('ignore'), None)
        self.assertEqual(codecs.lookup_error('ignore'),
                         (codecs.ignore_errors, None, None))

        # Test the replace error handler
        self.assertEqual(codecs.register_error('replace',
                                               codecs.replace_errors), None)
        self.assertEqual(codecs.lookup_error('replace'),
                         (codecs.replace_errors, None, None))

        # Test the xmlcharrefreplace error handler
        self.assertEqual(codecs
