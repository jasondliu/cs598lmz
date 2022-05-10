import _struct
# Test _struct.Struct.{pack,unpack}
# (Don't use from _struct import *; bad things can happen, like infinite
# recursion.)
from _struct import Struct, error
import unittest
from test import support
import sys
import ctypes
import itertools

class StructTest(unittest.TestCase):
    # Format strings and expected results for big-/little-endian
    # standard size and non-standard size items.
    # Each entry is a tuple: (format_string, expected_result).
    # There are 2 expected results: 1st for big-endian, 2nd for little.
    fmt_results = [
        ('xcbxhxhiix',
         ('\x00\x00\x11\x00\x22\x00\x33\x00\x44\x00'
          '\x55\x00\x66\x00\x77\x00\x88\x00\x99\x00',

          '\x00\x00\x22\x00\x44\x00\x66\x00\
