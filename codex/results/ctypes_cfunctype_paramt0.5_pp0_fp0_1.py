import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Wrap the C library
def wrap(lib):
    lib.fun.argtypes = [ctypes.c_double]
    lib.fun.restype = ctypes.c_double
    lib.fun.errcheck = errcheck

# Load the library, and wrap the function
lib = ctypes.CDLL('./libfun.so')
wrap(lib)

# Create a ctypes function object
c_fun = FUNTYPE(lib.fun)

# Call the function
print c_fun(1.0)
</code>
And this is the C code:
<code>#include &lt;stdio.h&gt;
#include &lt;math.h&gt;

double fun(double x) {
    return sin(x);
}
</code>
This works fine, but I would like to be able to pass additional arguments to the C function, for example:
<code>#include &lt;stdio.h&gt;
#include &lt;math.h&gt;


