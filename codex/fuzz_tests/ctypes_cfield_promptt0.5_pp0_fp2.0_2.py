import ctypes
# Test ctypes.CField.

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        super(A, self).__init__()

    def __repr__(self):
        return "<A instance at %x: a=%d, b=%d>" % (id(self), self.a, self.b)

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c_a", ctypes.CField("a")),
                ("c_b", ctypes.CField("b"))]
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        super(B, self).__init__()

    def __repr__(self):
        return
