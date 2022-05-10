import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short

s = S()

print s.x
print s.y

print ctypes.sizeof(s)
print ctypes.sizeof(s.x)
print ctypes.sizeof(s.y)
</code>
Output:
<code>0
0
4
2
2
</code>

