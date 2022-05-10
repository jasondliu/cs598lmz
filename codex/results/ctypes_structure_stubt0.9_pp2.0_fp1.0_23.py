import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s1 = S(1, 2)
s2 = S()
s2.x = 1
s2.y = 2

print(s1.x, s2.x)
print(s1.y, s2.y)
print(s1 == s2)
print(s1 is s2)
print(id(s1), id(s2))
print(ctypes.addressof(s1), ctypes.addressof(s2))
</code>

