import codecs
# Test codecs.register_error
# This test doesn't check the correct behaviour,
# it simply checks that the system doesn't crash
import test.support
import unittest
import sys
from codecs import lookup, BOM_UTF8, BOM_UTF16, BOM_UTF32
from test.support import findfile, run_unittest
from test.support import unlink, import_module

class CodecsModuleTest(unittest.TestCase):

    def test_utf7(self):
        self.assertEqual('+ABA-'.encode('utf-7'), b'+ABA-')
        self.assertEqual('\u20ac'.encode('utf-7'), b'+AOQ-')
        self.assertEqual('+AOQ-'.decode('utf-7'), '\u20ac')
        self.assertEqual(b'+AOQ-'.decode('utf-7'), '\u20ac')
        self.assertEqual('+ACI- +ADY- +AGA- +AHw- +AIM- +AKM- +AL
