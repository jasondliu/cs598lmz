import ctypes
# Test ctypes.CField
class IntStruct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

p = ctypes.pointer(IntStruct())
p.contents.a = 5
p.contents.b = 6

if p.contents.a != 5:
    raise ValueError("Failed to set a")

if p.contents.b != 6:
    raise ValueError("Failed to set b")

if p[0].a != 5:
    raise ValueError("Failed to get a")

if p[0].b != 6:
    raise ValueError("Failed to get b")

if p[0]["a"] != 5:
    raise ValueError("Failed to get a")

if p[0]["b"] != 6:
    raise ValueError("Failed to get b")

p[0]["a"] = 7
p[0]["b"] = 8

if p[0].a != 7:
    raise ValueError("Failed to set a")
