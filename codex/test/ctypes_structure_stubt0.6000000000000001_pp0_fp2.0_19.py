import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double.in_dll(ctypes.pythonapi, '_Py_NotImplementedStruct')

print(S.x)
