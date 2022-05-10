import codecs
# Test codecs.register_error

import codecs
import unittest
from test import test_support

@unittest.skipUnless(test_support.HAVE_UNICODE_FILE, 'requires Unicode file support')
class CodecsModuleTest(unittest.TestCase):
    def test_encode_decode(self):
        # codecs.encode() and codecs.decode()
        self.assertEqual(codecs.encode("abc"), "abc")
        self.assertEqual(codecs.encode(u"abc"), "abc")
        self.assertEqual(codecs.decode("abc"), u"abc")
        self.assertEqual(codecs.decode(u"abc"), u"abc")
        self.assertEqual(codecs.encode("abc", "rot-13"), "nop")
        self.assertRaises(TypeError, codecs.encode, 42)
        self.assertRaises(TypeError, codecs.decode, 42)

@unittest.skipUnless(test_support.HAVE
