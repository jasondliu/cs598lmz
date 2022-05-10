import codecs
# Test codecs.register_error in isolation:
import io
import os
import pickle
import sys
import tempfile
import unittest

import support

KEYWORD_MAP = {'replace': '?'}

class MockFileIO:

    def __init__(self, data, encoding='utf-8'):
        self.encoding = encoding
        self.buffer = io.BytesIO(data.encode(encoding))

    def read(self):
        return self.buffer.read().decode(self.encoding)

    def write(self, data):
        self.buffer.write(data.encode(self.encoding))

    def close(self):
        pass

class StrictTest(unittest.TestCase):
    def test_decode(self):
        for encoding in ('ascii', 'iso-8859-1'):
            self.assertRaises(UnicodeDecodeError, codecs.decode, b'\xff', encoding, 'strict')

    def test_encode(self):
        for encoding in ('ascii', 'iso-
