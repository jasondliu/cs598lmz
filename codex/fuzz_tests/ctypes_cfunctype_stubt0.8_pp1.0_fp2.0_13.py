import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.pythonapi.PyFloat_AsDouble.restype(ctypes.py_object)
print fun()
</code>
Returns None.  I believe PyFloat_AsDouble takes a PyObject* argument, so I don't see why I can't find the restype PyDouble object.
Also, if someone could explain to me the types of each of the objects being returned by <code>PyObject_Type</code>, <code>PyTypeObject</code>, <code>PyObject</code>, and <code>PyDouble</code>, it would be greatly appreciated.  I have looked into the docs, but I've been unable to find the information I need to know.  My first guess would be that all <code>Py</code> objects are pointers, but that's just a guess.


A:

First off: <code>PyObject_Type</code> and <code>Py_Type</code> are the same function. And when you get a pointer to a structure, you need to declare that in C, too. So you want to write something like:
<code>pythonapi.PyObject_Type.restype = c
