import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int + 1

p = create_string_buffer(20)
q = cast(p, POINTER(S))
q[1].x = 1
