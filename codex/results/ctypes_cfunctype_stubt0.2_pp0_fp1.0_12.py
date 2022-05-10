import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine.
However, if I try to return a list, I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ["hello"]

print(fun())
</code>
<blockquote>
<p>TypeError: 'list' does not have the buffer interface</p>
</blockquote>
I've tried using <code>ctypes.c_void_p</code> instead of <code>ctypes.py_object</code>, but that doesn't work either.
How can I return a list from a function that has a <code>CFUNCTYPE</code>?


A:

You can't.  The <code>CFUNCTYPE</code> is a C function pointer type.  It can only return a C type.  <code>py_object</code> is a C type, but <code>list</code> is not.  You can't return a Python object from
