import ctypes
class S(ctypes.Structure):
    x = ctypes.string_at(1, 4)
