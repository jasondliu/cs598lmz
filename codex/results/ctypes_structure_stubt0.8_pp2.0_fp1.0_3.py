import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short()
    y = ctypes.c_int()

s = S()
print(s.x, S.x.offset)
print(s.y, S.y.offset)
print(S.x.in_dll(ctypes.pythonapi, "PyStructSequence_Field"))
print(S.y.in_dll(ctypes.pythonapi, "PyStructSequence_Field"))
