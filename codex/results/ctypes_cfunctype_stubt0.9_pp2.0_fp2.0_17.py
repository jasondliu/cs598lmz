import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "a"

print fun()

#At this point, the type of 'fun' is not a py_object anymore,
#which means that the 'f' descriptor
#(same as the '__call__' attribute of a callable)
#doesn't know how to handle PyPy views.
f = fun.__call__

print f()

</code>
This works properly when passing PyPy views to CPython functions (PyPy object is converted to an equivalent CPython object). The problem comes when passing a CPython object to a PyPy function.
This code snippet will give a <code>BufferError</code> in PyPy:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(a, b):
    return ctypes.addressof(a)+ctypes.addressof(b)

print fun(1, 2)
</code>
In fact, the problem is that PyPy sees that the function passed is a CPython function (represented as a different type of <code>PyFunction</code
