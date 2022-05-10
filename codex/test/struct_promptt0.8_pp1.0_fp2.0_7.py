import _struct
# Test _struct.Struct objects, rather than the struct module
import struct as _structmodule
from UserList import UserList
from UserDict import UserDict
import weakref

from . _testcapi import INT_MAX
from unittest import TestCase, skipUnless, skipIf, run_unittest

from test import support
from test import mapping_tests
from test.support import import_helper, bigmemtest
from test.support.script_helper import assert_python_ok
import pickle

# This is a list of all the types and sizes in _struct.
_STRUCT_TYPES = [
    ("b", "B"),
    ("B", "B"),
    ("h", "H"),
    ("H", "I"),
    ("i", "i"),
    ("I", "I"),
    ("l", "l"),
    ("L", "L"),
    ("q", "q"),
    ("Q", "Q"),
    ("f", "f"),
    ("d", "d"),
]

# This is a list of all the types and sizes in _struct with alignment.
