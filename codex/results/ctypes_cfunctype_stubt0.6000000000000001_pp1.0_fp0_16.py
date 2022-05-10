import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(1)

def test_ctypes():
    print(fun())

if __name__ == "__main__":
    test_ctypes()
