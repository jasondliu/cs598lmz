import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char
    _fields_ = [("x", ctypes.c_char), ("y", ctypes.c_char)]

print(S.x)
print(S.y)
</code>
Output:
<code>&lt;Field type=c_char, ofs=0:0, size=1&gt;
&lt;Field type=c_char, ofs=1:1, size=1&gt;
</code>

