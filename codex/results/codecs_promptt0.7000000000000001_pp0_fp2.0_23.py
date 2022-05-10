import codecs
# Test codecs.register_error()

import codecs
import collections
import unittest

from test import test_support

class CodecRegistryTest(unittest.TestCase):

    def test_error_callback(self):

        # the default error callback
        def default_error_callback(error):
            raise error

        # define a dummy codec
        class DummyCodec(object):
            def encode(self, input, errors='strict'):
                return (input, len(input))

            def decode(self, input, errors='strict'):
                return (input, len(input))

        # register a dummy codec
        codecs.register(DummyCodec)

        # check that the default error handler is called
        self.assertRaises(UnicodeDecodeError,
                          '\n'.decode, 'ascii', 'strict')

        # check that the default error handler is called
        self.assertRaises(UnicodeDecodeError,
                          '\n'.decode, 'ascii', 'strict')

        # register a custom error handler

