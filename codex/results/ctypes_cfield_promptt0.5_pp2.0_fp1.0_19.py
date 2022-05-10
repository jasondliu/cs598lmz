import ctypes
# Test ctypes.CField.

# Create a structure with a pointer field.
class S(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(ctypes.c_int))]

# Create a pointer field.
pf = ctypes.CField(ctypes.POINTER(ctypes.c_int))

# Create a structure with the pointer field.
class T(ctypes.Structure):
    _fields_ = [("p", pf)]

# Use the pointer field.
t = T()
t.p = ctypes.POINTER(ctypes.c_int)()
t.p[0] = 12
print t.p[0] == 12

# Create a structure with a pointer field.
class U(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(ctypes.c_int))]

# Create a pointer field with a different name.
pf = ctypes.CField(ctypes.POINTER(ctypes.c_int), "q")

# Create a structure with the pointer field.
