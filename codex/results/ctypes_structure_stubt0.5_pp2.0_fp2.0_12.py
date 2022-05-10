import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class B(ctypes.Structure):
    _fields_ = [("s", S)]

class C(ctypes.Structure):
    _fields_ = [("b", B)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

a = E()
a.d.c.b.s.x = 2

b = a.d.c.b
b.s.x = 3

print(a.d.c.b.s.x)
</code>
Output:
<code>3
</code>
In this case, <code>a.d.c.b</code> and <code>b</code> are different objects, but they point to the same memory location.

