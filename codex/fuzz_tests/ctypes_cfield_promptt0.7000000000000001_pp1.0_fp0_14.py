import ctypes
# Test ctypes.CField
assert ctypes.CField.__name__ == 'CField'
# The following tests the __get__ method of a
# _CDataMeta.cdata_descriptor.
#
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

x = X()
x.a = 42
assert x.a == 42
#
# Test ctypes.CFuncPtr.
#
# A ctypes.CFuncPtr is a ctypes._CFuncPtr instance,
# which is a _Pointer instance, which is a subclass
# of int.
import _ctypes
assert isinstance(ctypes.CFuncPtr(None), _ctypes._CFuncPtr)
assert isinstance(ctypes.CFuncPtr(None), _ctypes._Pointer)
assert isinstance(ctypes.CFuncPtr(None), int)
import _ctypes_test
assert ctypes.CFuncPtr(_ctypes_test.get_errno) == _ctypes_test.get_errno
#
# Test ctypes.CData.
#
