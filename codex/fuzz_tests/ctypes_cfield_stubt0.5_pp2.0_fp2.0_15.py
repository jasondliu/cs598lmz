import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
</code>
I get
<code>&lt;Field type=i, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
</code>

