import weakref
# Test weakref.ref() and weakref.proxy() for strs
import gc
import operator
import pickle
import struct
import sys
import unittest
from test.support import run_unittest, TESTFN, check_py3k_warnings, is_jython
import test.support as support


class StrTest(unittest.TestCase):

    def test_hash(self):
        # See SF bug 528246:  Native string hash function differs from
        # Python's string hash function
        x = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10' \
            '\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"' \
            '#$%&\'()*+,-./0123456789:;<=>?@ABC
