import ctypes

class S(ctypes.Structure):
    x = [1, 2]
S._fields_ = [('X', ctypes.c_short*len(S.x))]
print S.x[1]

trace(length(S.X))
trace(length(S.x))
