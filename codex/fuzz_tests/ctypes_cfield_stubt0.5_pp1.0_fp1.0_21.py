import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyType(ctypes.CField):
    def __init__(self, *args, **kwds):
        super(MyType, self).__init__(*args, **kwds)

class S2(ctypes.Structure):
    _fields_ = [('x', MyType(ctypes.c_int))]

print(S2.x)
print(S2.x.__class__)

print(ctypes.sizeof(S))
print(ctypes.sizeof(S2))
</code>
Output:
<code>&lt;class '__main__.MyType'&gt;
&lt;class '__main__.MyType'&gt;
4
4
</code>

