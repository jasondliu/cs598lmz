import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_OptimizeFlag")

print(S.x)
