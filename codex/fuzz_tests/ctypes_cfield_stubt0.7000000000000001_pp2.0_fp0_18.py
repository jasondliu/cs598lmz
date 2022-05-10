import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(int):
    pass

for Base in (ctypes.c_int, int):
    for T in (X, Y):
        for Ptr in (ctypes.POINTER,):
            Type = Ptr(T)
            s = S()
            a = T(1)
            b = Base(2)
            x = Type(3)
            s.x = a
            assert type(s.x) is Base
            assert s.x == 1
            s.x = b
            assert type(s.x) is Base
            assert s.x == 2
            s.x = x
            assert type(s.x) is Base
            assert s.x == 3


# ctypes.c_void_p is not a subclass of int
