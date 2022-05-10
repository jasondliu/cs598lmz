import ctypes

class S(ctypes.Structure):
    x = (1,2,3)

s = S()

s.x = (4,5,6) # Fails, can't assign to tuple
