import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

def test_fun():
    assert fun() == "Hello World"

if __name__ == '__main__':
    test_fun()
</code>

