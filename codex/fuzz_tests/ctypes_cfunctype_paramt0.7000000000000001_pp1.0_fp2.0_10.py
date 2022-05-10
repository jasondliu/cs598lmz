import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

from contextlib import contextmanager
@contextmanager
def load_dll(dll_path):
    dll = ctypes.CDLL(dll_path)
    yield dll
    dll.free()

def run_dll_function(dll, call_name, func_type, *args):
    func = dll.__getattr__(call_name)
    func.argtypes = args
    func.restype = func_type
    return func(*args)

# run the dll function twice and print the results
with load_dll('../test_dll/test_dll.dll') as dll_test:
    func = FUNTYPE(lambda x: print(x))
    func('first')
    run_dll_function(dll_test, 'print_str', ctypes.c_int, func, 'second')
</code>
If you want to make your own <code>dll</code> you can do it the following way:

implement the desired functionality in C;
create a header file
