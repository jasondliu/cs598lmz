import ctypes
ctypes.cast(0, ctypes.py_object)
ctypes.pythonapi.PyCapsule_GetName.restype = ctypes.c_char_p
ctypes.pythonapi.PyCapsule_GetName.argtypes = [ctypes.py_object]
types = {'float32_t': 'float', 'float64_t': 'double'}
def cudatype(c): return types.get(ctypes.pythonapi.PyCapsule_GetName(c), ctypes.pythonapi.PyCapsule_GetName(c))

