import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
def make_func(func_ptr, nargs):
    # generate wrapper function with correct signature
    func = FUNTYPE(func_ptr) 

    return func

def call_func(func, arglist):
    # call wrapped function and return result
    return func(*arglist)
</code>
I get the following error:
<code>TypeError: must be type, not _ctypes.PyCFuncPtr
</code>
I am not sure what I am doing wrong here. Any hint would be highly appreciated.


A:

You get that error because <code>pass_func(func, arglist)</code> returns a function (what the <code>*func</code> does) but you don't want to pass that function. Instead, you want to pass the <code>arglist</code> you provide. The following code does that:
<code>from ctypes import *
from matplotlib.mlab import *

def pass_func(func, arglist):
    """Generate a function from a python function. In the
