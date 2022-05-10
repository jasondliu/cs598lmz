import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
</code>
Output:
<code>1 2
140731008299856
140731008299856
140731008299857
</code>

