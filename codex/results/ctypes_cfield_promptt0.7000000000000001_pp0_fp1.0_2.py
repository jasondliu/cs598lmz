import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int)]

class D(ctypes.Structure):
    class S(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_int),
                    ("c", ctypes.c_int)]

    _fields_ = [("foo", ctypes.c_int),
                ("bar", ctypes.c_int),
                ("x", S),
                ("y", S),
                ]
    _anonymous_ = ["x"]

class E(ctypes.Structure):
   
