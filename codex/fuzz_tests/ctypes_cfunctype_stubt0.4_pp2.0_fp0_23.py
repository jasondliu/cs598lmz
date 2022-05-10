import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
The error I'm getting is:
<code>TypeError: cannot convert the series to &lt;type 'int'&gt;
</code>
I'm not sure how to fix this.  I'm guessing it's something to do with the return type of the function, but I don't know what to change it to.
I'm using python 2.7.10.
Thanks.


A:

<code>ctypes</code> is not the right tool for this job.  It's designed to interface with C code, not Python code.  It's not surprising that it doesn't work.
If you want to call a Python function from C, use the <code>Python/C API</code>.  It's not pretty, but it's what you need.  This tutorial might help.

