import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print fun(1)
</code>
In my case I'm using this to convert a Python function to a C callback.  This works fine in Python 2.6 and Python 2.7 (and probably 2.5).  However, Python 3.x does not work.  Is there a way to make this work with Python 3.x?


A:

I don't think this is possible with the Python 2.x API.
The <code>Py_CallFunction</code> function doesn't support keyword arguments.  In Python 3, keyword arguments are passed to every callable.

