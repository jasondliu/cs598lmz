import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

def test_call_python_func_from_c():
    assert call_python_func_from_c(fun) == "hello world"


if __name__ == "__main__":
    import os
    import sys
    import py
    py.test.main(args=[os.path.abspath(__file__)] + sys.argv[1:])
