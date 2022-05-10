import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecRegressionTest(unittest.TestCase):
    def test_register_error(self):
        # SF bug #1174246:  codecs.register_error() didn't work
        # in 1.5.2
        def bad_handler(exception):
            raise exception
        codecs.register_error("test.notanencoding", bad_handler)
        self.assertRaises(UnicodeError, u'\u3042'.encode, "test.notanencoding")

def test_main():
    test_support.run_unittest(CodecRegressionTest)

