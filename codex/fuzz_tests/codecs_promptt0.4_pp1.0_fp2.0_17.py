import codecs
# Test codecs.register_error()

import unittest
from test import support

class CodecsModuleTest(unittest.TestCase):

    def test_bug_83495(self):
        # Test that we can register a custom error handler
        # with codecs.register_error()
        #
        # This test is copied from test_codecs.py.
        #
        # The original bug report (SF bug #83495) was that
        # registering a custom error handler with codecs.register_error()
        # failed with a SystemError.
        #
        # This test makes sure that the error handler is called with the
        # correct arguments, and that the correct exception is raised.
        #
        # The error handler is supposed to convert the input string to
        # output string and return a tuple (output string, length of
        # consumed input).  In this test, we simply use the 'replace'
        # error handler, which is available in every codec.
        import codecs
        def buggy_decode(input, errors='strict'):
            codecs.register_error('test.c
