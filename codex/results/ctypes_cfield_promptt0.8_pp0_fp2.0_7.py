import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [
        ("pad", ctypes.c_ubyte),
        ("a", ctypes.c_ubyte),
    ]
    def __init__(self, *args, **kw):
        ctypes.Structure.__init__(self, *args, **kw)
        self.a = 0
    def __repr__(self):
        return "X(%d, %d)" % (self.pad, self.a)

print X()

class XX(ctypes.Union):
    _fields_ = [
        ("pad", ctypes.c_ubyte),
        ("a", ctypes.c_ubyte),
    ]
    def __init__(self, *args, **kw):
        ctypes.Union.__init__(self, *args, **kw)
        self.a = 0
    def __repr__(self):
        return "XX(%d, %d)" % (self.pad, self.a)

print XX()

#
