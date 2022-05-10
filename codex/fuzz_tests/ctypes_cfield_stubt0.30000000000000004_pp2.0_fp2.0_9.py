import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyField(ctypes.CField):
    def __init__(self, *args, **kwargs):
        print("MyField.__init__", args, kwargs)
        super().__init__(*args, **kwargs)

ctypes.CField = MyField

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print(S2.x)
</code>
Output:
<code>MyField.__init__ ('x', &lt;class 'ctypes.c_int'&gt;) {}
MyField.__init__ ('x', &lt;class 'ctypes.c_int'&gt;) {}
&lt;Field type=c_long, ofs=0, size=4&gt;
</code>

