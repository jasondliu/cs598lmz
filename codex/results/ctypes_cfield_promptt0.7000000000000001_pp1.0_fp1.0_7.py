import ctypes
# Test ctypes.CField

import ctypes

class Test(ctypes.Structure):
    _fields_ = [("pad1", ctypes.c_byte),
                ("f1", ctypes.c_byte),
                ("pad2", ctypes.c_byte),
                ("f2", ctypes.c_byte)]

t = Test()
t.f1 = 1
t.f2 = 2
print(t.f1, t.f2) # 2 1

# Test ctypes.CField.from_address

import ctypes

class Test(ctypes.Structure):
    _fields_ = [("f1", ctypes.c_byte),
                ("f2", ctypes.c_byte)]

t = Test()
t.f1 = 1
t.f2 = 2

f = ctypes.CField.from_address(ctypes.addressof(t), ctypes.c_byte)
print(f.value) # 1
f.value = 3
print(t.f1) # 3

f = ctypes.CField.from_
