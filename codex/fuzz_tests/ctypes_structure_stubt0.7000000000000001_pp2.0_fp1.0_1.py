import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16
    _fields_ = [("x", ctypes.c_int16)]

z = S(x=0x10000)

print(z.x)
print(z.x == 0x10000)
</code>
output
<code>0
True
</code>

