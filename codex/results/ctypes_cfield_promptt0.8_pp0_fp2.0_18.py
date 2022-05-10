import ctypes
# Test ctypes.CField

import ctypes

class S(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int)]
    def __init__(self):
        self.f = 42

print(S().f)


class S2(ctypes.Structure):
    _fields_ = [("f", ctypes.CField)]
    def __init__(self):
        self.f = 42

print(S2().f)

class S3(ctypes.Structure):
    _fields_ = [("f", ctypes.CField(ctypes.c_int))]
    def __init__(self):
        self.f = 42

print(S3().f)

class S4(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 5)]
    def __init__(self):
        for i in range(5):
            self.a[i] = i

s4 = S4()
for i in range(5):
    assert s4.a[i] ==
