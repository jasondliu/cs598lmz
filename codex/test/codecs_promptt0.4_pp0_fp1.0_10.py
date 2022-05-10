import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        def raise_exception(exc):
            raise exc

        codecs.register_error("test.raising_exception", raise_exception)
        self.assertEqual(codecs.lookup_error("test.raising_exception"),
                         raise_exception)

    def test_register_error_overwrite(self):
        # Test overwriting an error handler
        def raise_exception(exc):
            raise exc

        codecs.register_error("test.raising_exception", raise_exception)
        self.assertEqual(codecs.lookup_error("test.raising_exception"),
                         raise_exception)

        def ignore_exception(exc):
            pass

        codecs.register_error("test.raising_exception", ignore_exception)
