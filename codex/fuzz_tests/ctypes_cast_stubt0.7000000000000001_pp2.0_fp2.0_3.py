import ctypes
ctypes.cast(0, ctypes.py_object)
# Segmentation fault (core dumped)
</code>
This is the only example I could find of casting a null pointer to a python object. 
I also tried <code>ctypes.pythonapi.PyCapsule_New(ctypes.cast(0, ctypes.py_object), None, None)</code> and got a similar error.
What is the correct way to create a null python object in ctypes?


A:

You can't cast a <code>NULL</code> pointer to a <code>PyObject*</code> or a <code>PyCapsule*</code>.
The only way to represent a <code>NULL</code> pointer in Python would be to pass <code>None</code> as the parameter.

