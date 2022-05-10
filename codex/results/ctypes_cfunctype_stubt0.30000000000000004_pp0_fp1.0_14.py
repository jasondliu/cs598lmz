import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works fine. However, if I add a <code>return</code> statement to the function, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
    return "world"

fun()
</code>
This fails with:
<code>TypeError: cannot convert the result to a Python object
</code>
Why does this happen? How can I fix it?


A:

This is a bug in ctypes.
The problem is that the function is being compiled as a generator.  The <code>return</code> statement in a generator is not a <code>return</code> statement, it's a <code>yield</code> statement.  So the function is actually returning a generator object.  The <code>CFUNCTYPE</code> wrapper is trying to convert that to a Python object, and failing.
The workaround is to use <code>ctypes.pythonapi.PyObject_GetIter</
