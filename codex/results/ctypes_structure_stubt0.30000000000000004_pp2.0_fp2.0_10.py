import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s2 = S()
s2.x = s.x
s2.y = s.y

print s2.x, s2.y

s3 = S()
s3.x = s2.x
s3.y = s2.y

print s3.x, s3.y
</code>
Output:
<code>1 2
1 2
1 2
</code>

