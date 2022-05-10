import codecs
# Test codecs.register_error

import codecs
import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, "ignore")
        self.assertRaises(TypeError, codecs.register_error, "ignore", None)
        self.assertRaises(TypeError, codecs.register_error, "ignore", lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore", lambda x, y: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore", lambda x, y, z: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore", lambda x, y, z, t: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore", lambda x, y, z, t, u: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore",
