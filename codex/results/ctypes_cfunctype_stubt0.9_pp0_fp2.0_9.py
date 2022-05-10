import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "a" * 32 * 1024 * 1024

if __name__ == "__main__":
    fn = fun()
