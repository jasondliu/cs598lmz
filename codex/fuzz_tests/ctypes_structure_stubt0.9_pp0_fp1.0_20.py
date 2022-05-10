import ctypes

class S(ctypes.Structure):
    x = ()
assert S._fields_ == [('x', ctypes.c_void_p)]

class A(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int32)]
with pytest.raises(TypeError):
    class B(A):
        _fields_ = [("a", A)]

class C(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int32)]
assert C() == C(0)

class D(ctypes.Structure):
    _fields_ = [("d", ctypes.c_int32),
                ("e", ctypes.c_int32)]
assert D() == D(0, 0)

# from SF bug 962401
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long)]

class B(A):
    pass

class C(ctypes.Structure):
    _fields_ = [("b", B)]

assert C.b.offset == 0
assert C.b
