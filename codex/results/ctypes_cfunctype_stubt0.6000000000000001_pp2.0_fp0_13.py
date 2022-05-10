import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test():
    fun_ptr = ctypes.cast(fun, ctypes.c_void_p)
    return fun_ptr.value

print(test())
</code>
I'm trying to get the address of the function <code>fun</code> and I'm getting the correct address on Windows. Is there a way to get this address on Linux? I'm using Python 3.6.4.


A:

You can use <code>ctypes.addressof</code> to get the address of the function object, but that address is not useful.  You can't use it to call the function.
The address of the code that implements the function is not accessible to Python code.  The function object is a Python object, and it has a pointer to the code that implements it, but that pointer is not accessible.

