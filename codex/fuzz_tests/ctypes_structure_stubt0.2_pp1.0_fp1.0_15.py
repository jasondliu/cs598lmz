import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

print ctypes.sizeof(s)

print ctypes.addressof(s)

print ctypes.addressof(s.x)
print ctypes.addressof(s.y)
</code>
Output:
<code>1 2
8
140735452645504
140735452645504
140735452645508
</code>

