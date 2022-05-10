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

        def bad_decode(input, errors='strict'):
            raise UnicodeError, "decoding error"
        def bad_encode(input, errors='strict'):
            raise UnicodeError, "encoding error"
        def ignore_encode(input, errors='strict'):
            return (input, len(input))
        def ignore_decode(input, errors='strict'):
            return (u"\ufffd", len(input))
        def replace_encode(input, errors='strict'):
            return (u"?", len(input))
        def replace_decode(input, errors='strict'):
            return (u"\ufffd", len(input))
        def xmlcharref
