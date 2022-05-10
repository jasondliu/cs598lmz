import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)

s = S()
print s.x
s.x = ctypes.c_int(1)
print s.x

s.x = ctypes.c_int(2)
print s.x

s.x = ctypes.c_int(3)
print s.x
</code>
prints:
<code>0
1
2
3
</code>

