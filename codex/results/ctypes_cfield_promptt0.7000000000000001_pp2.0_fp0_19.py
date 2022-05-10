import ctypes
# Test ctypes.CField
#
# CDataType_from_ctypes is used to convert ctypes types to ctypes_configure
# types.

import ctypes
from ctypes.test import is_resource_enabled

ctypes_test = ctypes.CDLL(ctypes.util.find_library("c"))

def test_CField():
    import _ctypes_test
    from ctypes import c_short, c_int, c_long, c_ushort, c_uint, c_ulong
    from ctypes import c_float, c_double

    class Test(ctypes.Structure):
        _fields_ = [("a", c_int)]

    if is_resource_enabled("printing"):
        print(repr(Test.a))
    assert repr(Test.a) == "<Field type=c_int, ofs=0, size=4>"

    assert Test.a.offset == 0
    assert Test.a.size == ctypes.sizeof(c_int)

    class Test(ctypes.Structure):
        _pack_ = 1
        _
