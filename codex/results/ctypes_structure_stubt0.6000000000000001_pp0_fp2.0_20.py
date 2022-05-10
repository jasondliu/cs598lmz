import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16
    y = ctypes.c_int32

s = S()

s.x = 0
s.y = 1

print(s.x)
print(s.y)

print(s.x.value)
print(s.y.value)
</code>
Output:
<code>0
1
0
1
</code>

