import codecs
# Test codecs.register_error()

from test import test_support
import unittest
from StringIO import StringIO
from codecs import register_error
from codecs import lookup

test_support.import_module('struct')

def make_replacement_handler(replacement):
    def handler(u, start, end):
        return replacement, end
    return handler

class TestBase:

    def assert_encode_decode(self, encodings, errors, input, output, *args):
        for encoding in encodings:
            for error in errors:
                # encode
                if isinstance(input, str):
                    encoded = input.encode(encoding, error, *args)
                    self.assertEqual(encoded, output)
                else:
                    self.assertRaises(UnicodeEncodeError, input.encode,
                                      encoding, error, *args)
                # decode
                if isinstance(output, str):
                    decoded = output.decode(encoding, error, *args)
                    self.assertEqual(decoded, input)
                else
