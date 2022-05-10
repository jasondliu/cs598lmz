import codecs
# Test codecs.register_error
#
# This test is based on the test_codecs.py test_register_error()
# test.

import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error()
        import codecs
        import string
        import sys

