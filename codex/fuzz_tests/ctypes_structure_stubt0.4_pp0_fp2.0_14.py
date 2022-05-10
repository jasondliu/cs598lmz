import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print s.x.value
print s.y.value
print s.z.value

s.x.value = 1
s.y.value = 2
s.z.value = 3

print s.x.value
print s.y.value
print s.z.value
</code>

