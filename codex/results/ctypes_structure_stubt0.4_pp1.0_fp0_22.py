import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    pass

print D.x
print D().x
print D.x.__class__
print D.x.__get__(D(), D)
print D.x.__get__(D(), D).__class__
print D.x.__get__(D(), D) is D.x

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class D(S):
    pass

print D.x
print D().x
print D.x.__class__
print D.x.__get__(D(), D)
print D.x.__get__(D(), D).__class__
print D.x.__get__(D(), D) is D.x
