import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(T.x)
print(T.x.__class__)
print(T.x.__class__.__name__)
print(isinstance(T.x, ctypes.CField))
print(isinstance(T.x, ctypes.Field))
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
CField
True
True
</code>

