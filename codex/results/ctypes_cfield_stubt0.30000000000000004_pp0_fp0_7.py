import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(type(C.x))
print(C.x.__class__)
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.Field'&gt;
&lt;class 'ctypes.Field'&gt;
</code>

