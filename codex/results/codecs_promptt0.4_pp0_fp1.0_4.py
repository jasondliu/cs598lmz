import codecs
# Test codecs.register_error

# This is a test for the codecs module.

import codecs
import unittest

class CodecsRegisterErrorTest(unittest.TestCase):
    def test_register_error(self):
        def xxtest1(exc):
            if isinstance(exc, UnicodeEncodeError):
                x = exc.object[exc.start:exc.end]
                return (u'!', exc.end)
            elif isinstance(exc, UnicodeDecodeError):
                return (u'!', exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test1", xxtest1)
        self.assertEqual(codecs.lookup_error("test1"), xxtest1)
        self.assertEqual(codecs.lookup_error("test2"), None)
        codecs.register_error("test2", None)
        self.assertEqual(codecs.lookup_error("test2"), None)
        codecs.register
