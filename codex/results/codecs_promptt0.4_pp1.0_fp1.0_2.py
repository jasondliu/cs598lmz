import codecs
# Test codecs.register_error

import unittest

class TestCodecs(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        import codecs
        import string
        import sys

        class TestError(Exception):
            pass

        def testfunc(errors):
            def raiseError(message):
                raise TestError(message)
            return raiseError

        codecs.register_error("test.notanencoding", testfunc)
        self.assertRaises(TestError, codecs.lookup_error, "test.notanencoding")

        codecs.register_error("test.notanencoding", testfunc)
        self.assertRaises(TestError, codecs.lookup_error, "test.notanencoding")

        codecs.register_error("test.code", testfunc)
        self.assertRaises(TestError, codecs.lookup_error, "test.code")

        codecs.register_error("test.code", testfunc)
        self.assertRaises(TestError, codec
