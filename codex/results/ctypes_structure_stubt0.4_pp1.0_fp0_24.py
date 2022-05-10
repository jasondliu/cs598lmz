import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print s.x
print s.y
print s.z

s.x = 4
s.y = 5
s.z = 6

print s.x
print s.y
print s.z
</code>
Output:
<code>1
2
3
4
5
6
</code>

