import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("c", ctypes.c_char)]

class T(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int),
                ("c", ctypes.CField(C))]

class U(ctypes.Structure):
    _fields_ = [("c", ctypes.CField(C)),
                ("i", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("t", T),
                ("c", ctypes.CField(C))]

class W(ctypes.Structure):
    _fields_ = [("t", T),
                ("u", U),
                ("c", ctypes.CField(C))]

class X(ctypes.Structure):
    _fields_ = [("c", ctypes.CField(C)),
                ("t", T),
                ("u", U)]

class Y(ctypes.Structure):
    _fields_ = [("c",
