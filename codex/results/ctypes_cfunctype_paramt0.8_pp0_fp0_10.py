import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)  # this must be declared outside of the function
def int_func(x):
    print('int_func({})'.format(x))
    return x
#Python has a wrapper for a C function pointer, which is a FUNCTYPE instance. 
func_var = FUNTYPE(int_func)
func_var(123)
</code>
This is described in the A Note on Python's <code>ctypes</code> module (by Sean Reifschneider)

