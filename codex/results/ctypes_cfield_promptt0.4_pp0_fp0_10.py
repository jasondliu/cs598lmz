import ctypes
# Test ctypes.CField
try:
    ctypes.CField
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test ctypes.CField.from_address()
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

s = S()
s.a = 42
f = ctypes.CField.from_address(id(s), "a")
print(f.get_int(s))
f.set_int(s, 24)
print(s.a)

# Test ctypes.CField.from_param()
class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

s = S2()
s.a = 42
f = ctypes.CField.from_param(s, "a")
print(f.get_int(s))
f.set_int(s, 24)
print(s.a)

# Test ctypes.CField.from_buffer()
class S3(ctypes.Structure
