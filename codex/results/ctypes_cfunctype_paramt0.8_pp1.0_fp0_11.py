import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def callable_python():
    print('callable_python')

call_ptr = FUNTYPE(callable_python)
#callable_python.argtypes = []
#callable_python.restype = None
call_ptr()
</code>
This has a drawback - the user defined function needs to have a 'void' or 'None' return type.

