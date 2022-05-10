import codecs
# Test codecs.register_error()

# Test utf-8 with unicode decode errors reported as UnicodeError.
# Test latin-1 with unicode decode errors reported as UnicodeError.
# Test error handling with unicode decode errors reported as UnicodeError.
# Test error handling with unicode decode errors reported as UnicodeDecodeError.
import codecs
import sys
import unittest

class UnicodeErrorTest(unittest.TestCase):
    # Note: some tests depend on _test1.py being encoded in UTF-8
    def test_file(self):
        with open(__file__, 'rb') as f:
            for func in (codecs.utf_8_decode, codecs.utf_8_encode):
                f.seek(0)
                self.assertRaises(UnicodeError, func, f.read())

    def test_streamwriter(self):
        class IncrementalEncoder(codecs.IncrementalEncoder):
            def encode(self, input, final=False):
                return codecs.utf_8_encode(input, final)[0]
        utf
