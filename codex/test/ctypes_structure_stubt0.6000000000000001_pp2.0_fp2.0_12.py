import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 3

S.__str__ = lambda self: str(self.x)

s = S()
print(s)
