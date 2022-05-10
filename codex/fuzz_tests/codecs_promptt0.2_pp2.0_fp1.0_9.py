import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        def g(exc):
            return (u"", exc.end)
        codecs.register_error("test.strict", g)
        self.assertEqual(codecs.lookup_error("test.strict"), g)
        def f(exc):
            if isinstance(exc, UnicodeDecodeError):
                self.assertEqual(exc.object, b"abc")
                self.assertEqual(exc.start, 0)
                self.assertEqual(exc.end, 3)
                self.assertEqual(exc.reason, "ouch")
                self.assertEqual(exc.encoding, "ascii")
                self.assertEqual(exc.args, (b"abc", 0, 3, "ouch"))
            elif isinstance(exc, UnicodeEncodeError):
                self.assertEqual(exc.object, u"abc")

