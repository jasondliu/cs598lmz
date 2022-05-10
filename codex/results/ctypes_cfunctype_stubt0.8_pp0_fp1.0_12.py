import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
fun()
</code>
However, using ctypes.byref(fun) doesn't work in the same way, I get the error:
<code>TypeError: argument 1 must be c_void_p, not function
</code>
I would like to create a function pointer with the same signature as the function and use it as an argument to a C function.


A:

I know this is old, but I ran into a similar problem...
AFAIK, You can't use ctypes.byref().  However, if all you want is to pass a pointer to your c/python function to a C/C++ function, you can do this:
<code>class FunPtr(ctypes.c_void_p):
    def __init__(self,func,functype=None):
        if functype is None:
            functype = ctypes.CFUNCTYPE(ctypes.c_int)
        ctypes.c_void_p.__init__(self,functype(func))
    def __call__(self,*args):
        return c
