import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

print(C.y)
print(C.y.__class__)
print(C.y.__class__.__bases__)
print(C.y.__class__.__bases__[0].__subclasses__())

print(C.y.__class__.__bases__[0].__subclasses__()[0](S, 'x'))
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;class '_ctypes.CField'&gt;
(&lt;class '_ctypes.Field'&gt;,)
[&lt;class '_ctypes._CData_value_'&gt;, &lt;class '_ctypes._Pointer_value_'&gt;]
&lt;Field type=c_int, ofs=0, size=4&gt;
</code>
If you're interested in the
