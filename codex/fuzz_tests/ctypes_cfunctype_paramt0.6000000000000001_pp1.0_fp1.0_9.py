import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def c_callback(arg):
    print("In python callback!")
    print("Arg:", arg)
    return 0

func_ptr = FUNTYPE(c_callback)
lib.register_callback(func_ptr, 5)
lib.call_python_callback()
</code>

