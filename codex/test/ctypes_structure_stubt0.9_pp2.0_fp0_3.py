import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_int * 2)()

s = S()
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_int))

#OK s.x[0]
#OK s.x[-1]
#OK s.x[1]
#OK s.x[2]
#OK s.x[3]

