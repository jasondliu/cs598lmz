import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s._fields_)
print(s._fields_[0][0])
print(s._fields_[1][0])
</code>
Output:
<code>1 2
[('x', &lt;class 'ctypes.c_int'&gt;), ('y', &lt;class 'ctypes.c_int'&gt;)]
x
y
</code>

