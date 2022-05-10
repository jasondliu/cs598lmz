import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

s = ctypes.pythonapi.PyTuple_New.argtypes

if __name__ == '__main__':
    print(ctypes.pythonapi.PyTuple_New.argstypes)
    print(ctypes.pythonapi.PyTuple_New.restype)
