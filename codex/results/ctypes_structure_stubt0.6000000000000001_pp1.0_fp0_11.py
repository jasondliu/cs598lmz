import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 100
s.y = 200

print s.x
print s.y

print s.x + s.y

print ctypes.sizeof(S)
print ctypes.sizeof(s)
print ctypes.sizeof(s.x)
print ctypes.sizeof(s.y)
</code>
This will give you the following output:
<code>100
200
300
8
8
4
4
</code>

