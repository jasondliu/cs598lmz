import ctypes
# Test ctypes.CField
    class A(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.CField, "a+2"),
                    ("c", ctypes.c_int)]
    a = A()
    a.a = 1
    assert a.b == 3
    assert a.c == 0
    a.b = 9
    assert a.a == 9
    assert a.c == 0
    a.c = 7
    assert a.a == 7
    assert a.b == 7 + 2
    print "TEST: ctypes.CField OK"


# Test structs inside structs inside structs.
    class B(ctypes.Structure):
        _fields_ = [("first", ctypes.c_int),
                    ("last", ctypes.c_int)]
    class C(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int),
                    ("y", ctypes.c_int),
                    ("z", ctypes.c_int),
                    ("str
