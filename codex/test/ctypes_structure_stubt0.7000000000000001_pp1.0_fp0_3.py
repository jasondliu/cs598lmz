import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class O(object):
    x = ctypes.c_int

so = S()
oo = O()

so.x = 42
oo.x = 42

print(so.x)
print(oo.x)
