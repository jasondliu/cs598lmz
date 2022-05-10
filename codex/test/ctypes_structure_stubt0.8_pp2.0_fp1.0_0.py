import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    z = [3, 4]

print(S.z)
print(S.z[0])
