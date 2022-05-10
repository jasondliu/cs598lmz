import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ctypes.CField("z", ctypes.c_int),
                ]
    def __repr__(self):
        return "<C %s>" % (self.__dict__,)

print C.x
print C.y
print C.z

c = C()
print c
print c.x
print c.y
print c.z

c.x = 1
c.y = 2
c.z = 3
print c

print ctypes.sizeof(C)
print ctypes.addressof(c)
print ctypes.addressof(c.x)
print ctypes.addressof(c.y)
print ctypes.addressof(c.z)
 
# Test alignment
import sys

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_
