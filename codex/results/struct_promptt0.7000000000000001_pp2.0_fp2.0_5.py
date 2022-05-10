import _struct
# Test _struct.Struct.pack_into() and unpack_from()
from test import support
import unittest
import warnings
from sys import byteorder
from test.support import bigmemtest, requires_32b
from test import test_struct

# The test strings used for testing all integer types and sizes.
pack_test_strings = [
    b'',
    b'\0',
    b'\0\0',
    b'\0\0\0',
    b'\0\0\0\0',
    b'\0\0\0\0\0',
    b'\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\
