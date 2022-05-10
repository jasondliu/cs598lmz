import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# ctypes.CFuncPtrType = ctypes.CFUNCTYPE

# _________________________________________________________________________

# This test is not appropriate for 64-bit
if WORD == 4:

    from ctypes import c_int

    class S1(ctypes.Structure):
        pass
    S1._fields_ = [("a", c_int), ("b", c_int)]

    class S2(ctypes.Structure):
        pass
    S2._fields_ = [("a", c_int),
                   ("b", c_int),
                   ("c", c_int),
                   ("d", c_int)]

    class S3(ctypes.Union):
        pass
    S3._fields_ = [("a", c_int),
                   ("b", c_int),
                   ("c", c_int),
                   ("d", c_int),
                   ("e", c_int),
                   ("f", c_int),
                   ("g", c_int)]

    class M1(ctypes.Structure):
        _fields_ = [("s
