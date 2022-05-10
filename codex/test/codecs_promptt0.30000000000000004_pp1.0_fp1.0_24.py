import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecRegressionTest(unittest.TestCase):

    def test_bug_117612(self):
        # This used to segfault.
        codecs.register_error("ignore", codecs.ignore_errors)

    def test_bug_13891(self):
        # This used to raise a SystemError.
        codecs.register_error("ignore", codecs.ignore_errors)

    def test_bug_3445(self):
        # This used to raise a SystemError.
        codecs.register_error("ignore", codecs.ignore_errors)

    def test_bug_4945(self):
        # This used to raise a SystemError.
        codecs.register_error("ignore", codecs.ignore_errors)

    def test_bug_4945(self):
        # This used to raise a SystemError.
        codecs.register_error("ignore", codecs.ignore_errors)

