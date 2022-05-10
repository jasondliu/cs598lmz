import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 10
s.y = 20

print s.x, s.y
print s.__dict__
print s._fields_

print ctypes.sizeof(s)
print ctypes.addressof(s)
print ctypes.addressof(s.x)
print ctypes.addressof(s.y)

print ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s))
print ctypes.string_at(ctypes.addressof(s.x), ctypes.sizeof(s.x))
print ctypes.string_at(ctypes.addressof(s.y), ctypes.sizeof(s.y))
</code>
Output:
<code>10 20
{}
[('x', &lt;class 'ctypes.c_int'&gt;), ('y', &lt;class 'ctypes.c_int'&gt;)]
8
14072855
