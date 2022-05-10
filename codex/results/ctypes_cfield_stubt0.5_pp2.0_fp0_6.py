import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 42

c = C()

# This works
ctypes.cast(id(c.x), ctypes.POINTER(ctypes.c_int)).contents.value

# This fails
ctypes.cast(id(c.x), ctypes.POINTER(ctypes.CField)).contents.value
</code>

