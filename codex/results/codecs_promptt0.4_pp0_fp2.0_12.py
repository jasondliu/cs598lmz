import codecs
# Test codecs.register_error
# This test is based on the test_codecs.py test_register_error()

# Note that the test is different than the C version, since Python
# doesn't have a way to specify the exact error handler to use.

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def bad_handler(exception):
            raise exception
        # Registering a bad handler should raise a TypeError
        self.assertRaises(TypeError, codecs.register_error, 'bad', bad_handler)
        # Registering a good handler should work
        codecs.register_error('good', lambda x: (x, len(x)))
        # Now check that it works
        self.assertEqual(codecs.strict_errors, 'strict')
        self.assertEqual(codecs.replace_errors, 'replace')
        self.assertEqual(codecs.ignore_errors, 'ignore')
        self.assertEqual(codecs.xmlcharrefreplace_
