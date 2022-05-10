import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("z", ctypes.c_int),
    ]

print(S.x)
print(S.y)
print(S.z)
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;Field type=c_int, ofs=4, size=4&gt;
&lt;Field type=c_int, ofs=8, size=4&gt;
</code>

