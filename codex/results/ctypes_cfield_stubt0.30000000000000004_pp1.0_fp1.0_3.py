import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

print C.y
print C.y.__class__
print C.y.__class__.__name__
print C.y.__class__.__module__
print C.y.__class__.__bases__
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
CField
ctypes
(&lt;type 'object'&gt;,)
</code>

