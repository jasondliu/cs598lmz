import ctypes
# Test ctypes.CField.from_address()
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
t = T()
t.s = s

print(ctypes.CField.from_address(t, "s"))
print(ctypes.CField.from_address(t, "s.a"))

# Test ctypes.CField.from_param()
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
t = T()
t.s = s

print(ctypes.CField.from_param(t.s))
print(ctypes.CField.from_param(t.s.a))

# Test ctypes.CField.in_dll()
class S(ctypes.Structure):
    _
