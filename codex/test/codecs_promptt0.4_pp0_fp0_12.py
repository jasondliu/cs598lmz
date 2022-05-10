import codecs
# Test codecs.register_error
#
# This test was written by Michael Hudson.
#
# Note that the test is not entirely self-contained; it assumes that
# the codecs module is working correctly, and that the codecs
# registered in the module are correct.
#
# This test is not exhaustive.

import codecs
import unittest
import string

# Some codecs to test with

class BaseCodec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

class StreamWriter(BaseCodec, codecs.StreamWriter):
    pass

class StreamReader(BaseCodec, codecs.StreamReader):
    pass

