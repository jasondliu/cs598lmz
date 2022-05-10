import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]
    def foo(self):
        return self.x
assert isinstance(X.x, ctypes.CField)
x = X()
assert x.foo().__class__ == X
# Test n_string
assert ctypes._pointer_t(None).n_string() == 'NULL'
import sys
if sys.implementation.name == 'pypy':
    assert ctypes._pointer_t(None)._cdata is None
    assert ctypes.POINTER(ctypes.c_byte)(None)._cdata is None
else:
    assert ctypes._pointer_t(None)._cdata == 0
    assert ctypes.POINTER(ctypes.c_byte)(None)._cdata == 0
check(ctypes.c_void_p)
check(ctypes.c_char, 'c')
check(ctypes.c_byte, 'b')
check(ctypes.c_ubyte, 'B')
check(ctypes.c_
