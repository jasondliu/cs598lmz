fn = lambda: None
gi = (i for i in ())
fn.__code__ = f.__code__
fn.__name__ = f.__name__

# ... and then run the tests.

import unittest
import sys
from test import support

class Test(unittest.TestCase):
    def test_module(self):
        self.assertEqual(inspect.getmodule(f), sys.modules[__name__])
        self.assertEqual(inspect.getmodule(fn), sys.modules[__name__])
        self.assertEqual(inspect.getmodule(c), sys.modules[__name__])
        self.assertEqual(inspect.getmodule(c()), sys.modules[__name__])
        self.assertEqual(inspect.getmodule(m), sys.modules[__name__])
        self.assertEqual(inspect.getmodule(gi), sys.modules[__name__])

    def test_defining_frame(self):
        self.assertEqual(inspect.getmodule(inspect.currentframe()), sys.modules[__name__])
        self.assertEqual
