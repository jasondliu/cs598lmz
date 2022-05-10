import codecs
# Test codecs.register_error
#
# This test is intended to be run under the control of regrtest.py.
#
# This test exercises the codecs.register_error function.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).

import codecs
import unittest

class RegisterErrorTest(unittest.TestCase):

    def test_register_error(self):
        # Test registering a simple error handler
        def handler(exception):
            return (u'', exception.start+1)
        codecs.register_error('test.simple', handler)
        # Test registering a complex error handler
        def handler(exception):
            return (u'', exception.start+1)
        codecs.register_error('test.complex', handler)
        # Test registering an error handler with a wrong type
        self.assertRaises(TypeError, codecs.register_error, 'test.wrong', 'foo')
        # Test registering an error handler with a wrong type
