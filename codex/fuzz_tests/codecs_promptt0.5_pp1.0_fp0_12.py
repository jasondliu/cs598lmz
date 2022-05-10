import codecs
# Test codecs.register_error

import codecs
import unittest
import StringIO

class CodecRegressionTest(unittest.TestCase):

    def test_bug_1228(self):
        # codecs.register_error() should not raise a TypeError
        # if the error handler is None
        codecs.register_error(None)

def test_main():
    test_support.run_unittest(CodecRegressionTest)

if __name__ == "__main__":
    test_main()
