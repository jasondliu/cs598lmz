import codecs
# Test codecs.register_error
# Failed to understand the following message in the test file: Warning: (test_codecs.py:testEncoderCallback, line 684)
# File "test_codecs.py", line 684, in testEncoderCallback
# self.assertRaises(UnicodeEncodeError, encode, "xyz\u20a0", "replace", callback=self._complain_cb)
#
# This test invokes a codec that is registered in the module.
# The internal codecs implementation is supposed to cover this.
#

import codecs
import unittest

class Test_Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)

