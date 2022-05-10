import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): print "Hello world"

fun()
callbacks.append(fun)
</code>
None of these callbacks works, so I would like to understand what it is that I am doing wrong with regards to the manipulation of the external functions in Python or to my understanding of the C code.
If I am not doing anything wrong and this is not the right example I would like to know if it is possible to just manipulate some function(s) by just using a simplified "Hello world" wrapper using Python.


A:

When you return the function <code>NULL</code> is returned, the Python C-API doesn't automatically convert this to <code>None</code> for some reason. This means that the callback is actually <code>None</code> (not a function).
Either return <code>Py_None</code> or use <code>PyErr_SetString</code> to raise an exception.

