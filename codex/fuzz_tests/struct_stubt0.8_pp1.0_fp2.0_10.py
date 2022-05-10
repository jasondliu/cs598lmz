from _struct import Struct
s = Struct.__new__(Struct)
s.pack_into("cchh", b"0", 2, 3)

from _struct import Struct
from _testcapi import string_as_buffer
Struct("cchh").pack_into(string_as_buffer(""), 0, 2, 3)


#from test.libregrtest.refleak import InputFile, RefleakTesting
from refleak import RefleakTesting
from struct import Struct
from _testcapi import string_as_buffer
from test.support import TESTFN

from test.libregrtest.refleak import RefleakTesting, InputFile

import sys
import struct
import unittest


def _format_code(object):
    """
    Returns the format code for a Struct object
    """
    return object._fmt.decode()


class FormatStringTests(unittest.TestCase):
    def test_format_codes(self):
        # Issue #21342
        for code in 'bBhHiIlLqQfd':
            Struct('=' + code)
            Struct('<' + code)
