import codecs
# Test codecs.register_error
from test import test_support
import unittest
from weakref import proxy

from test.test_support import run_unittest

class CodecsModuleTest(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(codecs.encode("abc"), ("abc", 3))
        self.assertEqual(codecs.encode("abc", "rot-13"), ("nop", 3))
        self.assertEqual(codecs.encode("abc", "rot-13", "strict"), ("nop", 3))
        self.assertEqual(codecs.encode("abc", "rot-13", "ignore"), ("nop", 3))
        self.assertEqual(codecs.encode("abc", "rot-13", "replace"),
                         ("nop", 3))
        self.assertEqual(codecs.encode("abc", "rot-13", "xmlcharrefreplace"),
                         ("nop", 3))
        self.assertRaises(TypeError, codecs.encode
