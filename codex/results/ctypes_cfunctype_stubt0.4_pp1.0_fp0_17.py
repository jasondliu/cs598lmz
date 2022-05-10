import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_ctypes():
    print(fun())

if __name__ == '__main__':
    test_ctypes()
