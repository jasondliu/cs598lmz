import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    
# A

a = S()
a.x = 10

print(a.x)

# B

b = S()
print(b.x)

# C

c = S(2)
print(c.x)
