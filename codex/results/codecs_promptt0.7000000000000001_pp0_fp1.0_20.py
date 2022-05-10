import codecs
# Test codecs.register_error
import sys
import random
import os
import unittest
import re
from test import test_support

import warnings
warnings.filterwarnings("ignore", "^codecs.cp.* is deprecated$")

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test the standard ErrorHandler implementations
        self.assertEqual(codecs.strict_errors(u'\uFFFE'), (u'\uFFFE', 1))
        self.assertEqual(codecs.ignore_errors(u'\uFFFE'), (u'', 1))
        self.assertEqual(codecs.replace_errors(u'\uFFFE'), (u'\uFFFD', 1))
        self.assertEqual(codecs.xmlcharrefreplace_errors(u'\uFFFE'),
                         (u'&#xFFFE;', 1))

        # Test a custom ErrorHandler
        def custom_handler(errors):
            def custom_error_handler(exception):
                self.assertE
