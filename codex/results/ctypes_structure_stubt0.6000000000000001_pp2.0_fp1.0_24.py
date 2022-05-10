import ctypes

class S(ctypes.Structure):
    x = 1,
    y = 2,

s = S()
for i in s._fields_:
    print(i)
</code>
Output:
<code>('x', c_int)
('y', c_int)
</code>

