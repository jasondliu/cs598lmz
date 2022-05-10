import ctypes
# Test ctypes.CFUNCTYPE(...)(...).
print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x)(3))
# Test ctypes._CFuncPtr(...).
print(ctypes._CFuncPtr.in_dll(ctypes, 'PyCFuncPtr_Type')(lambda x: x)(3))
# Test ctypes.pythonapi.PyCFunction_NewEx(...).
PyCFunction_NewEx = ctypes.pythonapi.PyCFunction_NewEx
PyCFunction_NewEx.argtypes = [ctypes.py_object, ctypes.py_object, ctypes.py_object]
PyCFunction_NewEx.restype = ctypes.py_object
print(PyCFunction_NewEx(None, None, lambda x: x)(3))

# Test ctypes.pythonapi.PyCapsule_New(...).
PyCapsule_New = ctypes.pythonapi.PyCapsule_New
PyCapsule_New.argtypes = [ctypes.c_void_p, ctypes.c_char_p, c
