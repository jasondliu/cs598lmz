import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)

# the following is equivalent to:
#   s = S(x=1)
s = S()

