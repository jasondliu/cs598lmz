import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

s2 = S()
s2.x = 1
s2.y = 2
s2.z = 3

print(s == s2)
print(s == s)

print(s is s2)
print(s is s)
</code>
Output:
<code>False
True
False
True
</code>

