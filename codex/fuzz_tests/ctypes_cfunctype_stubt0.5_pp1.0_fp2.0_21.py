import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print(fun())
</code>
But this gives me the following error:
<code>TypeError: The result type of the callback is not supported.
</code>
I have tried many different combinations of return types, but so far I haven't been able to get anything to work.
I'm using Python 3.4.3.


A:

The error message is misleading. The problem is that the callback must return a <code>PyObject*</code>, but <code>ctypes.py_object</code> is not a <code>PyObject*</code>.
Here is a working version:
<code>import ctypes

PyObject_CallFunction = ctypes.pythonapi.PyObject_CallFunction
PyObject_CallFunction.restype = ctypes.py_object
PyObject_CallFunction.argtypes = (ctypes.py_object, ctypes.c_char_p)

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

@FUNTYPE
def fun():
    return PyObject_CallFunction(None, b"
