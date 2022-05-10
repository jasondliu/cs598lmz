import codecs
# Test codecs.register_error:
from test import test_support

def g(s):
    return codecs.escape_decode(s)[0]

def f(s):
    return g(s)

def h(s):
    return codecs.escape_decode(s)[0]

def i(s):
    return codecs.escape_encode(s)[0]

class TestError(unittest.TestCase):

    def test_strict(self):
        # strict errors
        self.assertRaises(ValueError, g, "\\")
        self.assertRaises(ValueError, g, "\\x")
        self.assertRaises(ValueError, g, "\\x1")
        self.assertRaises(ValueError, g, "\\x1z")
        self.assertRaises(ValueError, g, "\\u")
        self.assertRaises(ValueError, g, "\\u1")
        self.assertRaises(ValueError, g, "\\u12")
        self.assertRaises(ValueError, g, "\\u
