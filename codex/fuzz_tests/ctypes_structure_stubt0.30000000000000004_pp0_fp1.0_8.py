import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print s.x, s.y, s.z

s1 = S()
s1.x = 4
s1.y = 5
s1.z = 6

print s1.x, s1.y, s1.z

print s.x, s.y, s.z
</code>
Output:
<code>1 2 3
4 5 6
1 2 3
</code>

