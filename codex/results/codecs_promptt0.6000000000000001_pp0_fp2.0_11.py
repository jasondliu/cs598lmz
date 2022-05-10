import codecs
# Test codecs.register_error()

from test import test_support

import codecs
import sys
import unittest

from test.test_support import run_unittest

class SimpleCodingMap:
    def __init__(self, map):
        self.map = map
    def encode(self, input, errors='strict'):
        return ''.join([self.map[c] for c in input]), len(input)
    def decode(self, input, errors='strict'):
        return ''.join([k for k, v in self.map.items() if v == c])
    def getregentry(self):
        return codecs.CodecInfo(
            name = 'test',
            encode = self.encode,
            decode = self.decode,
        )

class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        # This is a smoke test only; the actual tests are in test_codecs.
        c = SimpleCodingMap({'a': 'b'})
        codecs.register
