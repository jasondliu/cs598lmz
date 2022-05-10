import ctypes
# Test ctypes.CField.  This tests all the basic functionality of Field, as
# CField subclasses it, adding no extra functionality.  There are extra
# tests below to test the extra CField features.

# XXX: The tests here are very similar to the tests in test_field.py,
# except that they use ctypes.CField.  In the future, it might be better
# to keep a single base class for all the Field tests, and subclass it
# for these tests, so we can reuse the tests.

from ctypes import *
from test.test_support import run_unittest
from test.test_support import import_module

import sys

# Module that defines the fields and structs used in the tests.
test_fields_module = import_module('test_fields')

from test_fields_module import TestStruct, TestStructPtr


class TestCField(test_fields_module.TestField):
    '''Tests for ctypes.CField.  Tests all the basic functionality of Field,
    as CField subclasses Field, adding no extra functionality.  There are
    extra tests below to test
