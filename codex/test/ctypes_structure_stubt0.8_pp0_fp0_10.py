import ctypes

class S(ctypes.Structure):
    x = 1

s = S()

# This line is the source of the memory error
ctypes.pointer(s)

del s
