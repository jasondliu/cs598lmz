import codecs
# Test codecs.register_error/lookup_error

# This tests the 'backslashreplace' error handler.

import codecs
import sys

def check(input, expected):
    t = codecs.lookup_error('backslashreplace')
    res = t.__call__(input, 'strict')
    if res != expected:
        raise ValueError("unexpected result: got %a, expected %a" %
                         (res, expected))

# Simple codec (codecs.charmap_build should work too)
class BackslashReplaceTest(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors,
                                     {ord('\xaa'): '\\xaa'})
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors,
                                     {ord('\xaa'): '\\xaa'})
codecs.register(BackslashReplaceTest)

# Test cases
