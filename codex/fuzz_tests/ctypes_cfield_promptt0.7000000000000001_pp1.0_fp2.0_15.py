import ctypes
# Test ctypes.CField.__init__(*args, **kw)
#
# Note: the _fields_ list is a dummy,
#       we only access the instance attributes.
#
# This class is used to test the ctypes.CField.__init__ method.


class Foo(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', ctypes.c_int)]
    _anonymous_ = ['test']

    def __init__(self, *args, **kw):
        ctypes.Structure.__init__(self, *args, **kw)
        self.test = ctypes.c_int(42)
        self.b = ctypes.c_int(42)
        self.c = ctypes.c_int(42)


class Bar(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int)]
    _anonymous_ = ['test']

    def __init
