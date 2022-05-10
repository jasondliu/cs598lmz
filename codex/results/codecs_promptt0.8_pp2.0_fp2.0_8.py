import codecs
# Test codecs.register_error
from test import test_support
import unittest

class TestCodecsRegisterError(unittest.TestCase):

    def test_lookup_unknown(self):
        self.assertEqual(codecs.lookup_error("blahblah"),
                         (None, None))
        self.assertEqual(codecs.lookup_error("blahblah"),
                         (None, None))

    def test_strict(self):
        self.assertEqual(codecs.strict_errors(ord("A"), "replace"),
                         (u"?", 1))
        self.assertEqual(codecs.strict_errors(ord("A"), "ignore"),
                         (u"", 0))
        self.assertEqual(codecs.strict_errors(ord("A"), "xmlcharrefreplace"),
                         (u"&#65;", 1))
        self.assertEqual(codecs.strict_errors(ord("A"), "backslashreplace"),
                         (u"\\x41", 1))

    def test_
