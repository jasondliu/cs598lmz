import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 5

s = S()
s.x[0] = 1
s.x[1] = 2
s.x[2] = 3
s.x[3] = 4
s.x[4] = 5

print s.x[0]
print s.x[1]
print s.x[2]
print s.x[3]
print s.x[4]
</code>
The output is:
<code>1
2
3
4
5
</code>

