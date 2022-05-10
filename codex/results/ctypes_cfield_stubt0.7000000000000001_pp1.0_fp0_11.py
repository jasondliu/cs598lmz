import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class D(C):
    _fields_ = [('x', ctypes.c_int)]

s = S()
print(type(s.x))
print(s.x.__class__)
print(type(D.y))
print(D.y.__class__)
print(D.x.__class__)
</code>
output:
<code>&lt;class '_ctypes.CField'&gt;
&lt;class '_ctypes.CField'&gt;
&lt;class '_ctypes.CField'&gt;
&lt;class '_ctypes.CField'&gt;
&lt;class '_ctypes.CField'&gt;
</code>

