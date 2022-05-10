import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

##r = ctypes.c_int()
##assert "ctypes." not in repr(r), repr(r)

##r = ctypes.py_object()
##assert "ctypes." not in repr(r), repr(r)

##r = ctypes.c_float(1.0)
##assert "ctypes." not in repr(r), repr(r)
##

##r = ctypes.POINTER(ctypes.c_int)()
##assert "ctypes." not in repr(r), repr(r)

##r = ctypes.POINTER(ctypes.c_int)()
##assert "ctypes." not in repr(r), repr(r)

# Issue 1144850
##r = ctypes.c_int(9)
##r = ctypes.pointer(r)
##assert "ctypes." not in repr(r), repr(r)

# Issue 1145072
##r = ctypes.pointer(ctypes.c_int(9))
##assert "ctypes." not in repr(r), repr(r)
