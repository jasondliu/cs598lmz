import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# http://sourceforge.net/p/ctypes/bugs/146/
# this fails with an AttributeError:
# ctypes.CField(object(), ctypes.c_int)

# XXX I don't know if this is the right behavior, but it is
# different from the original one:

print ctypes.CField(object(), ctypes.c_int)
ctypes.CField(object(), ctypes.c_int)
