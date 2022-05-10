import codecs
# Test codecs.register_error
import _testcapi
import sys
import unittest


class CodecRegressionTest(unittest.TestCase):
    def test_main(self):
        # Testing the "register_error" API
        def bad_decode(input, errors='strict'):
            raise UnicodeDecodeError("unknown", input, 42, 43, "ouch")

        def bad_encode(input, errors='strict'):
            raise UnicodeEncodeError("unknown", input, 42, 43, "ouch")

        def ignore_decode(input, errors='strict'):
            return (u"\ufffd", len(input))

        def ignore_encode(input, errors='strict'):
            return (str("?"), len(input))

        def replace_decode(input, errors='strict'):
            return (u"\ufffd" * len(input), len(input))

        def replace_encode(input, errors='strict'):
            return (str("?") * len(input), len(input))

