import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
S_p = ctypes.POINTER(S)
s = S()
s.x = 42
s_p = S_p(s)
s_p.x = 42

class A(ctypes.Structure):
    _fields_ = [
        ('s', S_p)
    ]
a = A()
a.s = s_p
a.s.contents.x = 42
</code>
Yet another alternative is to use <code>ctypes.byref</code>:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 42

class A(ctypes.Structure):
    _fields_ = [
        ('s', ctypes.POINTER(S))
    ]

a = A()
a.s = ctypes.byref(s)
a.s.contents.x = 42
</code>

