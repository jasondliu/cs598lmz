import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

def test():
    f = S.in_dll(ctypes.py_object(ctypes.py_object()), "x")
    print(f.value)

test()
</code>

