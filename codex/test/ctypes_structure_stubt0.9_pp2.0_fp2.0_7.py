import ctypes

class S(ctypes.Structure):
    x = 1
    def a(self):
        return 42

S._anonymous_ = ['a']

print(S.x)
print(S().a())
