import ctypes
# Test ctypes.CField - class and instance

class C(ctypes.Structure):
    _fields_ = [('value', ctypes.c_int)]

class P(C):
    _fields_ = [('pointer', ctypes.POINTER(C))]

o = C(10)
p = C(20)

# Give the class P a 'pointer' attribute
P.pointer = ctypes.field(P, 'pointer', ctypes.POINTER(C))

m = P(5)
print(m.value, m.pointer._obj.value)

m.value = 6
print(m.value, m.pointer._obj.value)

m.pointer._obj.value = 7
print(m.pointer._obj.value)

m.pointer._obj = p
print(m.pointer._obj.value)

print(m.pointer.contents.value)
