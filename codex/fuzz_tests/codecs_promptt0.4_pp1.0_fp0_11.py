import codecs
# Test codecs.register_error

# This test is meant to be run with -uall.

import codecs
import test.support
import unittest

# Test encoders and decoders
class CodecTest(unittest.TestCase):
    def test_register_error(self):
        def bad_handler(exception):
            raise ValueError
        codecs.register_error('test.bad_handler', bad_handler)
        self.assertEqual(codecs.lookup_error('test.bad_handler'),
                         bad_handler)
        self.assertRaises(ValueError, codecs.lookup_error, 'test.bad_handler')

class TestBase(unittest.TestCase):
    def test_bad_handler(self):
        def bad_handler(exception):
            raise ValueError
        self.assertRaises(ValueError, codecs.lookup_error('test.bad_handler'))

    def test_invalid_errors(self):
        self.assertRaises(TypeError, codecs.lookup_error, 'strict')
       
