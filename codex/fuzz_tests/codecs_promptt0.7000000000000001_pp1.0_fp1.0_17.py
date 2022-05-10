import codecs
# Test codecs.register_error
# (also tests py_encode and py_decode in the process)

import codecs
import unittest
from test import support

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        class Codec(codecs.Codec):
            def encode(self, input, errors='strict'):
                return input, len(input)
            def decode(self, input, errors='strict'):
                return input, len(input)

        class IncrementalEncoder(codecs.IncrementalEncoder):
            def encode(self, input, final=False):
                return input
            def reset(self):
                pass

        class IncrementalDecoder(codecs.IncrementalDecoder):
            def decode(self, input, final=False):
                return input
            def reset(self):
                pass

        class StreamWriter(Codec, codecs.StreamWriter):
            pass

        class StreamReader(Codec, codecs.StreamReader):
            pass

        def search_function(encoding):
            if
