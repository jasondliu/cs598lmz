import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

s = S()
print(type(s.x))
c = C()
print(type(c.s.x))
</code>
Output:
<code>&lt;class 'ctypes.c_int'&gt;
&lt;class 'ctypes.c_int'&gt;
</code>

