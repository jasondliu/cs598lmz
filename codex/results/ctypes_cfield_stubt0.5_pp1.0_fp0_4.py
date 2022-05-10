import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

print(C())
print(C.y)
print(C.y.__class__)
print(C.y.__class__.__bases__)
print(C.y.__class__.__bases__[0].__bases__)
</code>
Output:
<code>&lt;__main__.C object at 0x7f6dfd3a8e80&gt;
&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class 'ctypes.CField'&gt;
(&lt;class 'ctypes.CField'&gt;,)
(&lt;class 'ctypes.Field'&gt;, &lt;class 'object'&gt;)
</code>

