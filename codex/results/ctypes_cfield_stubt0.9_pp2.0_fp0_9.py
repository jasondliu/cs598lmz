import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

lib = ctypes.CDLL("./libctypes_cfield.so")

init = lib.init

class A:
    pass

a = A()

init(ctypes.CField(a))

print a.b == 30
</code>
Compiled with GCC, this outputs:
<code>True
</code>

