import ctypes
# Test ctypes.CField
class c_foo(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int),
                ("bar", ctypes.c_int)]

c_f = c_foo(1, 2)

c_f.foo = 3
if c_f.foo != 3:
    raise RuntimeError("auto-c-int field failed")

c_f.bar = 4
if c_f.bar != 4:
    raise RuntimeError("auto-c-int field failed")

c_f.foo = -1
c_f.bar = -1

# Test ctypes.Field
class c_foo2(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

c_f2 = c_foo2(1)

c_f2.foo = 3
if c_f2.foo != 3:
    raise RuntimeError("auto-c-int field failed")

c_f2.foo = -1

class c_foo3(ctypes.Structure):
    _fields
