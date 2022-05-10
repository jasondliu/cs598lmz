import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64()
    y = ctypes.c_uint64()

s = S()

# I'd like to do something like this:
# s.x &= 0xFFFFFFFF
# s.y &= 0xFFFFFFFF
# but I can't figure out how to do it.
