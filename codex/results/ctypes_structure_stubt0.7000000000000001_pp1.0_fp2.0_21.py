import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_short)]

class U(ctypes.Union):
    x = ctypes.c_short
    y = ctypes.c_short
    _fields_ = [('x', ctypes.c_short), ('y', ctypes.c_short)]

class T(ctypes.Structure):
    s = S()
    u = U()
    _fields_ = [('s', S), ('u', U)]

print(ctypes.sizeof(S))
print(ctypes.sizeof(T))
print(ctypes.sizeof(ctypes.c_short))
</code>
prints
<code>4
8
2
</code>
So the structure S has a size of 4 and T has a size of 8, which is 4 + 4 = 2 * sizeof(S).

