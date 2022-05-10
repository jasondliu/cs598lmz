import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
I'm using Python 3.4.3 on Ubuntu 14.04, if that makes a difference.


A:

You can use <code>ctypes.cast(0, ctypes.py_object)</code> to get a <code>PyObject*</code> that is not a valid reference to an object.
I don't know what you are trying to do, but a <code>PyObject*</code> is not a <code>PyTypeObject*</code>, and you can't use it as one.
The only way to get a <code>PyTypeObject*</code> is to go through a <code>PyObject*</code> that is a type object.

