import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# New types can't derive from ctypes._SimpleCData any more.
# But they do inherit from ctypes._SimpleCData.
# In other words, this works:
class S2(ctypes._SimpleCData):
    _type_ = "i"
    def __init__(self):
        self._b_base_ = ctypes.addressof(self._buffer_)

class W(ctypes.Union):
    _fields_ = [('c', ctypes.c_char),
                ('i', ctypes.c_int)]

ctypes.UnionType = type(W.c)
ctypes.UnionCField = type(W.c)

ctypes.CArrayType = type(W.c * 3)
ctypes.CFuncPtrCallable = type(W.c.__call__)

# Verify that empty structures are not allowed,
# and structures with only pad bytes are brocken.
class Pad(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("pad", ctypes.c_int * 15
