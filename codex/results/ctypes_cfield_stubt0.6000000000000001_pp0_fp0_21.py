import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFoo(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

class CBar(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_int)]

def func(s):
    return s.foo

s = CFoo(1)
x = func(s)
print(x)

s = CBar(2)
x = func(s)
print(x)
</code>
It prints:
<code>1
2
</code>

