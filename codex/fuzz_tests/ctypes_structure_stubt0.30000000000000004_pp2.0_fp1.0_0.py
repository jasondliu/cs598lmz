import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

print S.x
print S.y
</code>
This prints:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;Field type=c_int, ofs=4, size=4&gt;
</code>
I would like to get the offset of the field as a number, not as a Field object. How can I do that?


A:

<code>print S.x.offset
print S.y.offset
</code>

