import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def f(x):
    return x**2

def f2(x):
    return x

# ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]

# l = [1,2,3,4,5]
# l_ptr = ctypes.pythonapi.PyCapsule_GetPointer(l, None)
# print(l_ptr)

# print(ctypes.c_void_p(l_ptr).value)

f_ctypes = FUNTYPE(f)
f2_ctypes = FUNTYPE(f2)
print(f_ctypes(100))

f_ptr = ctypes.pythonapi.PyCapsule_GetPointer(f_ctypes, None)
f2_ptr = ctypes.pythonapi.PyCapsule_GetPo
