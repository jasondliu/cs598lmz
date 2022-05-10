import codecs
# Test codecs.register_error

import codecs
import unittest

class Test_register_error(unittest.TestCase):

    class X:
        def __init__(self):
            self.called = 0
            self.exc = 0

        def __call__(self, errors=None):
            self.called += 1
            self.exc = errors
            return None, lambda x: x

    def test_register_error(self):
        x = self.X()
        codecs.register_error("test.x", x)
        self.assertEqual(x.called, 0)
        codecs.lookup_error("test.x")
        self.assertEqual(x.called, 1)
        codecs.lookup_error("test.x")
        self.assertEqual(x.called, 1)
        codecs.lookup_error("test.x")
        self.assertEqual(x.called, 1)
        s, h = codecs.lookup_error("test.x")
        self.assertEqual(x.called, 1)

