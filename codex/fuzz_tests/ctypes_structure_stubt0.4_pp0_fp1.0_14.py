import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

print S.x
print S.y
print S.z
</code>
prints:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
&lt;Field type=c_int, ofs=4, size=4&gt;
&lt;Field type=c_int, ofs=8, size=4&gt;
</code>
If you want to access the fields by name, you can use the <code>_fields_</code> attribute:
<code>&gt;&gt;&gt; S._fields_
(('x', c_int), ('y', c_int), ('z', c_int))
</code>

