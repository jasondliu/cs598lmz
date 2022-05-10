import ctypes
# Test ctypes.CField()
# We want to make sure that we can pass in a CField as
# a positional argument.

class X(ctypes.Structure):
    _fields_ = [
        ("a_f", ctypes.CField),
    ]
    def __init__(self, a_f):
        self.a_f = a_f

x = X(1)
print x.a_f
