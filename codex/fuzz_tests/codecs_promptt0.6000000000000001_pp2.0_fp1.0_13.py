import codecs
# Test codecs.register_error.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# 
# See the test case for details.
#

import unittest
from test import support
import codecs
from codecs import charmap_build, codecs_test_support

class TestCodecs(codecs_test_support.CodecsTestSupport, unittest.TestCase):

    def test_register_error(self):

        # Test a custom error handler
        def handler(error):
            return u'*', error.end+1

        codecs.register_error('myerror', handler)
        self.assertEqual(unicode('abc', 'ascii', 'myerror'), u'*b*c')

        # Test a custom error handler with a unicode exception argument
        def handler(error):
            return u'*', error.end+1

        codecs.register_error('myerror', handler)
        self.assertEqual(unicode('
