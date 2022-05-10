import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2.0))
</code>
This gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    f_c = FUNTYPE(f)
TypeError: must be real number, not function
</code>
This is the documentation for the <code>CFUNCTYPE</code> class:
<code>class ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
</code>
<blockquote>
<p>Create a C callable function prototype instance. The returned instance
  is callable and when called, creates and calls a C function that has
  the same calling convention as the Python function. The prototype of
  the C function is given by restype and argtypes. The prototype is
  converted to a ctypes
