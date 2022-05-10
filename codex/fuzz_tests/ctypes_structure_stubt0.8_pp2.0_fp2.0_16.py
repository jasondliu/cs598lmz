import ctypes

class S(ctypes.Structure):
    x = ctypes.union(ctypes.c_short, ctypes.c_char, ctypes.c_long)
    assert sizeof(S) == sizeof(ctypes.c_long)

class S2(ctypes.Structure):
    x = ctypes.union(ctypes.c_char, ctypes.c_short)
    assert sizeof(S2) == sizeof(ctypes.c_short)

class S3(ctypes.Structure):
    x = ctypes.union(ctypes.c_short, ctypes.c_char)
    assert sizeof(S3) == sizeof(ctypes.c_short)

class S4(ctypes.Structure):
    x = ctypes.union(ctypes.c_char, ctypes.c_short)
    assert sizeof(S4) == sizeof(ctypes.c_short)

class S5(ctypes.Structure):
    x = ctypes.union(ctypes.c_byte, ctypes.c_short)
    assert sizeof(S5) == sizeof(ctypes.c_short)
