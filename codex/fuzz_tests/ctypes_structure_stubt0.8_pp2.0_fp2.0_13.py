import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

class V(ctypes.Union):
    _fields_ = [
        ('arr', ctypes.c_double * 3),
        ('s', S)
    ]

print 'size of S', ctypes.sizeof(S)
print 'size of V', ctypes.sizeof(V)
</code>
which outputs
<code>size of S 24
size of V 3
</code>
So there's no overhead for unions.

