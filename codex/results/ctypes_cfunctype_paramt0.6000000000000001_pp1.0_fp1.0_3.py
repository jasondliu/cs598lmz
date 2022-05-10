import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def ff(x):
    return x**2

myCFunc = FUNTYPE(ff)

print(myCFunc(2))
</code>
I expect that the output should be 4 but it returns 8.


A:

You are passing a function with a <code>double</code> argument and returning a <code>double</code>.  It's the <code>cdecl</code> calling convention.  The C code that would generate your function would look like this:
<code>double ff(double x)
{
    return x * x;
}
</code>
The <code>ff</code> function takes a <code>double</code> argument and returns a <code>double</code>.  The C compiler produces assembly code that looks much like what you're doing in Python.  The first argument is passed in <code>xmm0</code>, the result is returned in <code>xmm0</code>.  The only difference is that the C compiler doesn't have to call a function.  If you wanted to pass a function pointer
