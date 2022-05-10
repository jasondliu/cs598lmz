import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))

def f(x, y, z, p):
    z[0] = x + y
    p[0] = x - y
    return 0

f_c = FUNTYPE(f)
print(f_c)
print(type(f_c))
</code>
This prints:
<code>&lt;__main__.CFUNCTYPE object at 0x7f1f3c3e6d18&gt;
&lt;class '__main__.CFUNCTYPE'&gt;
</code>
I'm trying to use <code>f_c</code> in a C++ function:
<code>#include &lt;iostream&gt;
#include &lt;cmath&gt;

extern "C"
{
    void f(double x, double y, double *z, double *p);
}


