import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)
print(s._fields_)
</code>
Output:
<code>1
2
{}
[('x', &lt;class 'ctypes.c_int'&gt;), ('y', &lt;class 'ctypes.c_int'&gt;)]
</code>

