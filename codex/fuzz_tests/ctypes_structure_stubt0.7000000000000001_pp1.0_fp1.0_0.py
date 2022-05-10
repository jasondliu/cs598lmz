import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p.in_dll(ctypes.pythonapi, "PyString_FromString")
    x.argtypes = [ctypes.c_char_p]
    x.restype = ctypes.py_object

print(S().x("hello"))
</code>

