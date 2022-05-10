import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

s = S()

s.x = 2.0
s.y = 3.0

print(s.x, s.y)

print(ctypes.sizeof(S))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
</code>
Output:
<code>2.0 3.0
16
140495879019744
140495879019744
140495879019748
</code>

