import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()

print(s.x)
print(s.x.value)
s.x.value = 2
print(s.x)
print(s.x.value)

# 1
# 1
# c_int(2)
# 2
