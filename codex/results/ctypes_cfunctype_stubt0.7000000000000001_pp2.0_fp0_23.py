import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
I get this error:
<code>RuntimeError: maximum recursion depth exceeded in __instancecheck__
</code>
It seems that my function is called again.
I am using Python 2.7.10 and Linux.
Why is this happening?


A:

You are using the wrong type, it is <code>CFUNCTYPE</code> not <code>CFUNCYTPE</code>.

