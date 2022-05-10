import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        #
        # This test is not very good, because it's hard to test that
        # the error handler is actually called.  For now, we just
        # check that the error handler is called with the right
        # arguments.
        #
        # XXX Should we add a test that the error handler is actually
        # called?
        def handler(exception):
            self.assertEqual(exception.__class__, UnicodeDecodeError)
            self.assertEqual(exception.encoding, "ascii")
            self.assertEqual(exception.object, b"\xff")
            self.assertEqual(exception.start, 0)
            self.assertEqual(exception.end, 1)
            return (u"\ufffd", 1)
        codecs.register_error("test.unicode_decode_error", handler)
        self
