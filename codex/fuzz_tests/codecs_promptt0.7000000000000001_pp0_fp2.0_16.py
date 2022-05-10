import codecs
# Test codecs.register_error, including the 'backslashreplace' handler.

import codecs
import os
import unittest

from test import support

try:
    codecs.lookup_error('surrogatepass')
except LookupError:
    raise unittest.SkipTest("'surrogatepass' error handler not available")


class TestBackslashreplace(unittest.TestCase):
    def test_all(self):
        for handling in ('strict', 'replace', 'ignore', 'surrogatepass',
                         'backslashreplace'):
            errors = codecs.lookup_error(handling)
            self.assertEqual(errors.handler_name, handling)
            self.assertEqual(errors.name, handling)
            self.assertEqual(errors.__name__, handling)
            self.assertEqual(errors('\uDC80'), '\\udc80')
            self.assertEqual(errors(b'\xf1'), '\\xf1')
            self.assertEqual(errors(b'\xff'), '\\xff')

   
