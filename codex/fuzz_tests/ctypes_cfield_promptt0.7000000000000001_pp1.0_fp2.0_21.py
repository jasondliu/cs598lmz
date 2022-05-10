import ctypes
# Test ctypes.CField
# Test CField.__str__

libc = CDLL(ctypes.util.find_library("c"))

class Test(ctypes.Structure):
    _fields_ = [
        ("f0", ctypes.c_int),
        ("f1", ctypes.c_int),
        ("f2", ctypes.c_int),
        ]

f0 = Test.f0
print(f0.__str__())
f1 = Test.f1
print(f1.__str__())
print(Test.f2.__str__())
