import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    @property
    def y(self):
        return self.x

print(S().y)
