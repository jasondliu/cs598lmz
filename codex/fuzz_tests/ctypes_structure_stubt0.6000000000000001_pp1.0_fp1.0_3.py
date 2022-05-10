import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [("s", S)]

c = C()
print c.s.x
c.s.x = 10
print c.s.x
</code>
This is the output I get:
<code>0
10
</code>

