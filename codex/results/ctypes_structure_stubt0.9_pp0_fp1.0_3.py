import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(3)

s = S()
print(typing.get_type_hints(s))
