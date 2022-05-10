import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def call_c(func, *args):
    args = [arg.ctype for arg in args]
    func = FUNTYPE(func)
    func(*args)

def test_call_python():
    assert call_python(some_python_function, 1, 2, 3) == 6

def test_call_c():
    call_c(some_c_function, 1, 2, 3)
</code>

