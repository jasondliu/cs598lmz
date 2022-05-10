import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1

s2 = copy.copy(s)
s2.y = 2

s3 = copy.deepcopy(s)
s3.z = 3

print s.x
print s.y
print s.z
print
print s2.x
print s2.y
print s2.z
print
print s3.x
print s3.y
print s3.z
</code>
produces
<code>1
0
0

1
2
0

1
2
3
</code>

