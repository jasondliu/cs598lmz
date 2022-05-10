import ctypes
# Test ctypes.CField
assert ctypes.CField.__name__ == 'CField'
f = ctypes.CField(ctypes.c_int, "foo")
assert f.__name__ == 'foo'
assert f.offset == 0
f = ctypes.CField(ctypes.c_int, "foo", 10)
assert f.offset == 10
assert repr(f) == "<Field type=c_int, ofs=10>"
# Test ctypes.CArrayType
assert ctypes.CArrayType.__name__ == 'CArrayType'
class S(ctypes.Structure):
    _fields_ = [("arr", ctypes.c_int * 2)]
s = S()
assert isinstance(s.arr, ctypes.CArrayType)
# Test ctypes.CFieldPointer
assert ctypes.CFieldPointer.__name__ == 'CFieldPointer'
class S(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(ctypes.c_int))]
s = S()
s.p = ctypes.pointer
