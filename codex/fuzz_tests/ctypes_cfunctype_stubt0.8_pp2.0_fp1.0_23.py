import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    ctypes.pythonapi.PyErr_SetObject(ctypes.py_object(SystemError), ctypes.py_object(SystemError("error")))
    return None
</code>
Here, the first argument of <code>PyErr_SetObject</code> is a PyObject; a <code>PyTypeObject *</code>.  The exception I'm raising is a <code>SystemError</code>, which is a class defined by Python.  However, I've never seen any documentation or code that uses or gets a pointer to a PyTypeObject.
This particular example works fine (it raises a SystemError exception), but I've seen a lot of code (including the example in the answer to this question: https://stackoverflow.com/a/7026987/3092) which just uses a function as the first argument to <code>PyErr_SetObject</code> like this:
<code>PyErr_SetObject(PyExc_IOError, Py_None);
</code>
None of that code ever seems to actually call <code>PyErr_SetObject</code> with the <code>Py
