import ctypes
# Test ctypes.CField and ctypes.Field
import _ctypes_test

try:
    unicode
except NameError:
    unicode = str

if hasattr(_ctypes_test, 'CFieldTest'):
    class CFieldTest(ctypes.Structure):
        _fields_ = [(_ctypes_test.CFieldTest, 'a'),
                    (_ctypes_test.CFieldTest, 'b')]

class FieldTest(ctypes.Structure):
    _fields_ = [('a', _ctypes_test.CFieldTest),
                ('b', _ctypes_test.CFieldTest)]

class FieldTest2(ctypes.Structure):
    _fields_ = [('a', FieldTest),
                ('b', FieldTest)]

class CFieldTest2(ctypes.Structure):
    _fields_ = [('a', CFieldTest),
                ('b', CFieldTest)]

class FieldTest3(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                (_ctypes_test.CFieldTest
