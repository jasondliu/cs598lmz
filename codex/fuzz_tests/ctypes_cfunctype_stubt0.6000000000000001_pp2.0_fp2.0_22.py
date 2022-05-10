import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
</code>
The above code is supposed to be a callback function of a C++ class. However, when I call this function in Python, it returns a NULL pointer. If I do not use ctypes.py_object as the return type, I will get the following error:
<code>TypeError: an integer is required (got type NoneType)
</code>
I have also tried ctypes.c_void_p as the return type and it returns a NULL pointer.
Is there a way to return a string from a callback function?


A:

The problem is that there is no way to return a <code>PyObject</code> from a callback function.
The documentation for <code>PyObject</code> says:
<blockquote>
<p>The base object type. All objects accessible from Python are instances of PyObject or of a subtype of PyObject.</p>
</blockquote>
That means that <code>PyObject</code> is an abstract data type, not a concrete type.  You can't create an instance of it, you can only create an instance of a subtype.  And Python
