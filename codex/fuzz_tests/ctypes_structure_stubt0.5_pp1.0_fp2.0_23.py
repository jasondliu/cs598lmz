import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()

print(s.x.value)
print(s.y.value)

s.x.value = 4

print(s.x.value)
print(s.y.value)
</code>

