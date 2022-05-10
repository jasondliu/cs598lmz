import ctypes
# Test ctypes.CField class

class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]

# Test ctypes.CField.__get__ and __set__:
p = POINT()
p.x = 1
p.y = 2
print(p.x, p.y)
try:
    p.x = 3.4
except TypeError:
    print("TypeError")
try:
    p.x = "test"
except TypeError:
    print("TypeError")

# Test ctypes.CField.from_address

class TEST(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]

p = POINT.from_address(ctypes.addressof(TEST()))
print(p.x, p.y)
