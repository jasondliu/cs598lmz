import codecs
# Test codecs.register_error()
import sys
import unittest
from test import support

class TestRegistryError(unittest.TestCase):
    def test_error_callback(self):
        # Test the error callback registry
        def replace1(exc):
            if not isinstance(exc, UnicodeDecodeError):
                raise TypeError("don't know how to handle %r" % exc)
            print('replace1 called')
            t = exc.object[exc.start:exc.end]
            return (u'\ufffd' * len(t), exc.end)
        def replace2(exc):
            if not isinstance(exc, UnicodeDecodeError):
                raise TypeError("don't know how to handle %r" % exc)
            print('replace2 called')
            t = exc.object[exc.start:exc.end]
            return (u'\ufffd' * len(t), exc.end)

        # Register the error handler first
        codecs.register_error('test.replace1', replace1)
        # Now load the codec
        with support.check_warnings
