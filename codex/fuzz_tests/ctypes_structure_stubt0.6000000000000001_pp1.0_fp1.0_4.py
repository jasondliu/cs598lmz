import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

s = S()
print(s.x)
print(s.y)
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
print(ctypes.sizeof(s))

# 0
# 0
# 139867243737984
# 139867243737984
# 139867243737992
# 16
</code>

