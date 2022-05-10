import io
# Test io.RawIOBase
import os
import sys
import tempfile
import unittest
from test import support

class TestRawIOBase(unittest.TestCase):
    def test_newlines(self):
        # Test newlines argument to open()
        def check_readline(f, newline, expected):
            f.seek(0)
            self.assertEqual(f.readline(None), expected)
        def check_readlines(f, newline, expected):
            f.seek(0)
            self.assertEqual(f.readlines(), expected)
        def check_writelines(f, newline, expected):
            f.seek(0)
            self.assertEqual(f.read(), expected)

        for newline in ('', '\n', '\r', '\r\n'):
            for chunk in ('', 'a', 'abc'):
                for chunks in ([chunk], [chunk, chunk]):
                    f = io.BytesIO()
                    f.writelines(chunks)
                    f.seek(0)
                    check_read
