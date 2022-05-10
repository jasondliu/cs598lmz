import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x*x

f_c = FUNTYPE(f)

f_c(2)
</code>
In this case, I get the following error:
<code>ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention
</code>
I've tried to look for the solution, but couldn't find anything. Any ideas how to fix this?


A:

You will need to specify the calling convention for <code>FUNTYPE</code> to match that used by the DLL.  Try this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double,
                           calling_convention='cdecl')

def f(x):
    return x*x

f_c = FUNTYPE(f)

f_c(2)
</code>

