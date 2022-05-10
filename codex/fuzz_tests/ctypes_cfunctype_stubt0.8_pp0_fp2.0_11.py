import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert call(fun) == 42

if __name__ == '__main__':
    test_double()
    test_fun()
    print('Passed all tests')
