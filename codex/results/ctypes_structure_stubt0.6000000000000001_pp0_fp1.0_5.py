import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
S._fields_ = [
    ('x', ctypes.c_int),
    ('y', ctypes.c_int),
]

s = S()

print s.x
print s.y

print s.x.__class__
print s.y.__class__

print type(s.x)
print type(s.y)

print s.x is s.y

print S.x
print S.y

print S.x.__class__
print S.y.__class__

print type(S.x)
print type(S.y)
</code>
Output:
<code>0
0
&lt;type 'c_long'&gt;
&lt;type 'c_long'&gt;
&lt;type 'c_long'&gt;
&lt;type 'c_long'&gt;
False
&lt;Field type=c_int, ofs=0:0, size=4&gt;
&
