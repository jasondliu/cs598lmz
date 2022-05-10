import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _pack_ = 2

class T(ctypes.Structure):
    _pack_ = 1
    y = ctypes.c_int
    s = S

t = T()
print (ctypes.sizeof(t))
</code>
Output:
<code>10
</code>

