import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # Copy the type object to avoid refleaking

class C(ctypes.Structure): pass
C._fields_ = [('f', ctypes.c_int)]

class D(C):
    _anonymous_ = ("f",)

class E(ctypes.Union):
    _fields_ = [('f', S)]

class D2(E): pass

class F(ctypes.Structure):
    _fields_ = [('f', D)]
    _anonymous_ = ("f",)

class G(ctypes.Structure):
    _fields_ = [('f', F)]

# F has a pointer to S within it, so S should be alive (as an object of type
# CField) even when F is deallocated. But the pointer to S must also be
# deallocated too, as the CField is not a registered gc type.
f = F()
ref = weakref.ref(f.f.x)
del f
gc.collect()
assert ref() is None

# G has a pointer to S within it, so S
