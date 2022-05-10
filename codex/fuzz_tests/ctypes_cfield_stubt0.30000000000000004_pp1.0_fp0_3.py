import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__bases__)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(D.x)
print(D.x.__class__)
print(D.x.__class__.__bases__)
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
(&lt;class 'ctypes.Field'&gt;,)
&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
(&lt;class 'ctypes.Field'&gt;,)
</code>

