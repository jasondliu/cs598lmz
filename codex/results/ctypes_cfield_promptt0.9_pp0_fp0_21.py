import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("aa", ctypes.c_uint8)]

a = A()
a.aa = 0x54
print(a.aa)
b = ctypes.cast(ctypes.pointer(a), ctypes.POINTER(ctypes.c_uint8))
print(b.contents.value)
print(a.aa)
print(hex(b.contents.value))
print(hex(a.aa))

c = b.contents

c.value = 0x55

print(a.aa)
print(hex(a.aa))

# Test os.listdir
import os

print(os.listdir("/"))

# Test os.stat

import os
print(os.stat("/proc/version"))
print(os.stat("/"))

# Test os.fdopen
import os, sys

fd = os.open("/proc/version", os.O_RDONLY)

f = os.fdopen(fd, "r")

# Test
