import codecs
# Test codecs.register_error('ignore') in TextIOWrapper.write()

import unittest
import os
import io
import sys

class TestWrite(unittest.TestCase):

    def test_write_ignore(self):
        # string of all 256 characters
        data = bytes(range(256))

        tmp = io.StringIO()

        # register a new error handler
        codecs.register_error('ignore', lambda e: ('', e.start + 1))
        with io.TextIOWrapper(tmp, encoding="ascii",
                              errors='ignore') as f:
            f.write(data.decode("utf-8"))

        self.assertEqual(tmp.getvalue(), '')

    def test_write_ignore_surrogates(self):
        # string of all 256 characters
        data = bytes(range(256))

        tmp = io.StringIO()

        # register a new error handler
        codecs.register_error('ignore', lambda e: ('', e.start + 1))
        with io.TextIOWrapper(tmp, encoding="utf
