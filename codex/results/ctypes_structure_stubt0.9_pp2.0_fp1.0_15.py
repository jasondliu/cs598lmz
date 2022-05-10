import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(ctypes.c_uint)

s = S()
a = ctypes.c_uint()
a.value = 5
s.y = ctypes.pointer(a)

while True:
    s.x += 1
    s.y[0] -= 1
    if s.y[0] &lt; 5:
        break
</code>

