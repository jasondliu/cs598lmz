import ctypes
# Test ctypes.CFUNCTYPE
#
# CFUNCTYPE does not have a complete test suite; all the tests
# for CFUNCTYPE are in test_ctypes.
#
# The tests are run on both Python and ctypes; the pytho one just
# to test the descriptor protocol, but the ctypes one is used to
# test the real functionality.
#
# The tests for the new callback feature are at the end of this
# file.

from ctypes import (CFUNCTYPE, c_char, c_int, c_void_p, c_double,
                    cast, POINTER, Structure, pythonapi, py_object)
from ctypes.util import find_library
import _ctypes
import unittest
import sys
import os

# On OSX, the system headers define a macro with the name "descriptor".
# This prevents the "type" variable from being set to the type "descriptor".
if sys.platform == "darwin":
    import ctypes.macholib.dyld
    ctypes.macholib.dyld.DEFINE_MACRO
