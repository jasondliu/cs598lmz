import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        exec(sys.argv[1])
